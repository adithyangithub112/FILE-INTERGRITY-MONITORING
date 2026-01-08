import requests
import json
import os

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")


def create_jira_ticket(title, description):
    if not all([JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN, PROJECT_KEY]):
        print("[ERROR] Jira environment variables not set")
        return

    url = f"{JIRA_URL}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": title,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{
                        "type": "text",
                        "text": description
                    }]
                }]
            },
            "issuetype": {"name": "Bug"}
        }
    }

    try:
        response = requests.post(
            url,
            auth=(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=10
        )

        if response.status_code != 201:
            print(f"[ERROR] Jira ticket creation failed: {response.text}")

    except requests.RequestException as e:
        print(f"[ERROR] Jira request error: {e}")
