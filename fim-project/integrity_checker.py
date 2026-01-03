import json
import os
import hashlib
from jira_integration import create_jira_ticket
from email_alert import send_email

BASELINE_FILE = "data/baseline_hashes.json"


def calculate_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def load_baseline():
    with open(BASELINE_FILE, "r") as f:
        return json.load(f)["files"]


def check_integrity():
    baseline = load_baseline()

    for file_path, old_hash in baseline.items():
        if not os.path.exists(file_path):
            continue

        new_hash = calculate_hash(file_path)
        if new_hash != old_hash:
            create_jira_ticket(file_path, old_hash, new_hash)
            send_email(file_path, old_hash, new_hash)
            print(f"🚨 Alert: {file_path}")


if __name__ == "__main__":
    check_integrity()
