import os
import json
import hashlib
from datetime import datetime

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


def generate_baseline():
    baseline = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            try:
                baseline[path] = get_metadata(path)
            except Exception as e:
                print(f"[ERROR] Skipping {path}: {e}")
    return baseline


def save_baseline(data):
    os.makedirs("data", exist_ok=True)
    with open(BASELINE_FILE, "w") as f:
        json.dump({
            "created_at": datetime.now().isoformat(),
            "files": data
        }, f, indent=4)
    print("Baseline created successfully")


if __name__ == "__main__":
    save_baseline(generate_baseline())
