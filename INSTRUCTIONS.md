## Commands Used for Environment Variable Setup (Linux)

### 1.Set Environment Variables Temporarily (Session Only)

```bash
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your_api_token"
export JIRA_PROJECT_KEY="FIM"

export ALERT_EMAIL="your_email@gmail.com"
export ALERT_EMAIL_PASSWORD="gmail_app_password"
export ALERT_EMAIL_RECEIVER="receiver@example.com"

```

⚠️ These variables are lost when the terminal is closed.

---

### 2.Set Environment Variables Permanently (Recommended)

Open the profile file:

```bash
nano ~/.profile

```

Add the following lines at the end:

```bash
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your_api_token"
export JIRA_PROJECT_KEY="FIM"

export ALERT_EMAIL="your_email@gmail.com"
export ALERT_EMAIL_PASSWORD="gmail_app_password"
export ALERT_EMAIL_RECEIVER="receiver@example.com"

```

Save and exit:

- `CTRL + O` → Enter
- `CTRL + X`

---

### 3. Reload Environment Variables (Without Logout)

```bash
source ~/.profile

```

---

### 4.Verify Environment Variables

```bash
echo$JIRA_URL
echo$JIRA_EMAIL

```

If values are printed, variables are loaded correctly.

## Cron Automation Setup (Linux)

---

### 1. Find Required Paths

```bash
which python3
pwd

```

Example output:

```
/usr/bin/python3
/home/kali/fim-project

```

---

### 2.Create Wrapper Script for Cron Execution

```bash
nano /home/kali/fim-project/run_fim.sh

```

```bash
#!/bin/bash
source /home/kali/.profile
cd /home/kali/fim-project ||exit 1
/usr/bin/python3 integrity_checker.py

```

Save and exit:

- `CTRL + O` → Enter
- `CTRL + X`

---

### 3. Make the Script Executable

```bash
chmod +x /home/kali/fim-project/run_fim.sh

```

---

### 4. Edit Crontab

```bash
crontab -e

```

Add the following line:

```bash
*/5 * * * * /home/kali/fim-project/run_fim.sh >> /home/kali/fim-project/fim.log 2>&1

```

---

### 5. Verify Cron Job

```bash
crontab -l

```

---

### 6. View Cron Execution Logs

```bash
cat /home/kali/fim-project/fim.log

```

---

## Cron Schedule Explanation

```
*/5 * * * *
│   │ │ │ │
│   │ │ │ └─ Day of week
│   │ │ │── Month
│   │ │──── Day of month
│   │────── Hour
└────────── Minute (every 5 minutes)

```
