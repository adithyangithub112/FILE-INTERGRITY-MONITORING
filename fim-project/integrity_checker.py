import os
import json
import hashlib
from datetime import datetime
from jira_integration import create_jira_ticket
from email_alert import send_email

MONITOR_DIR = "monitor_folder"
BASELINE_FILE = "data/baseline.json"


def calculate_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def get_metadata(path):
    stat = os.stat(path)
    return {
        "hash": calculate_hash(path),
        "mtime": stat.st_mtime,
        "ctime": stat.st_ctime
    }


def load_baseline():
    with open(BASELINE_FILE, "r") as f:
        return json.load(f)["files"]


def scan_current():
    current = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            try:
                current[path] = get_metadata(path)
            except Exception as e:
                print(f"[ERROR] Skipping {path}: {e}")
    return current


def alert(title, message):
    create_jira_ticket(title, message)
    send_email(title, message)


def check_integrity():
    baseline = load_baseline()
    current = scan_current()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Modified files
    for path, base_data in baseline.items():
        if path in current and base_data != current[path]:
            msg = f"""File Integrity Violation

Time: {timestamp}
File: {path}

Baseline: {base_data}
Current : {current[path]}
"""
            alert("File Integrity Violation", msg)

    # New files
    for path in current:
        if path not in baseline:
            alert(
                "New File Detected",
                f"Time: {timestamp}\nFile: {path}"
            )

    # Deleted files
    for path in baseline:
        if path not in current:
            alert(
                "File Deleted",
                f"Time: {timestamp}\nFile: {path}"
            )


if __name__ == "__main__":
    try:
        check_integrity()
    except Exception as e:
        print(f"[CRITICAL] Integrity check failed: {e}")
