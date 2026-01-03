import requests
import json
import os

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")


def create_jira_ticket(file_path, old_hash, new_hash):
    url = f"{JIRA_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": f"File Integrity Alert: {file_path}",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "type": "text",
                        "text": (
                            f"File modified:\n{file_path}\n\n"
                            f"Old Hash: {old_hash}\n"
                            f"New Hash: {new_hash}"
                        )
                    }]
                }]
            },
            "issuetype": {"name": "Bug"}
        }
    }

    requests.post(
        url,
        auth=(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
