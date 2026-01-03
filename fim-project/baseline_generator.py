import os
import hashlib
import json
from datetime import datetime

MONITOR_DIR = "monitor_folder"
BASELINE_FILE = "data/baseline_hashes.json"
HASH_ALGO = "sha256"


def calculate_hash(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_baseline():
    hashes = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            path = os.path.join(root, file)
            hashes[path] = calculate_hash(path)
    return hashes


def save_baseline(data):
    os.makedirs("data", exist_ok=True)
    with open(BASELINE_FILE, "w") as f:
        json.dump({
            "created_at": datetime.now().isoformat(),
            "algorithm": HASH_ALGO,
            "files": data
        }, f, indent=4)
    print("✅ Baseline created")


if __name__ == "__main__":
    save_baseline(generate_baseline())
