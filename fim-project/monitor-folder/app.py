"""
app.py
-------
Sample application file for File Integrity Monitoring (FIM).

This file represents a critical application component.
Any change to this file should trigger:
- Hash mismatch detection
- Jira ticket creation
- Email alert
"""

def get_app_status():
    """
    Returns the current status of the application.
    """
    return "Application is running normally"


def main():
    print("=== Sample Application ===")
    print(get_app_status())


if __name__ == "__main__":
    main()
