# File Integrity Monitoring System

## 1. Introduction

File Integrity Monitoring (FIM) is a security mechanism used to detect unauthorized changes to files and directories. It ensures that critical system and application files are not modified, deleted, or replaced without authorization.

This project implements a **Python-based File Integrity Monitoring system** with **automated alerting and ticket creation**.

## 2. Objectives

The main objectives of this project are:

- To monitor files in a specified directory
- To detect file modifications
- To calculate and compare cryptographic hashes of files
- To generate automated alerts using email
- To create incident tickets automatically in **Atlassian Jira**
- To run the monitoring process automatically using system scheduling

## 3. System Architecture

The system operates in two phases:

1. **Baseline Creation**
    - Initial hashes of monitored files are calculated
    - Hash values are stored in a JSON file
    - This baseline represents the trusted state of files
2. **Integrity Monitoring**
    - Current hashes of monitored files are calculated
    - Current hashes are compared with baseline hashes
    - Any mismatch indicates a file integrity violation

---

## 4. Technologies Used

- **Programming Language:** Python 3
- **Hashing Algorithm:** SHA-256
- **Data Storage:** JSON
- **Ticketing System:** Jira REST API
- **Alerting Mechanism:** Email (SMTP)
- **Automation:** Cron Jobs
- **Operating System:** Linux

---

## 5. Project Structure

```
fim-project/
│
├── monitor_folder/
│   └── app.py
│
├──data/
│   └── baseline_hashes.json
│
├── baseline_generator.py
├── integrity_checker.py
├── jira_integration.py
├── email_alert.py
└── requirements.txt

```

---

## 6. Module Description

### 6.1 Baseline Generator

- Iterates through all files in the monitored directory
- Calculates SHA-256 hash values
- Stores file paths and hashes in a JSON file
- Executed only once to establish a trusted baseline

---

### 6.2 Integrity Checker

- Loads baseline hash values from the JSON file
- Recalculates current hash values of monitored files
- Compares baseline and current hashes
- Detects only **file modifications**
- Triggers alerts if a hash mismatch is found

---

### 6.3 Jira Integration

- Uses Jira REST API for issue creation
- Automatically creates a ticket for each integrity violation
- Includes file path details in the ticket

---

### 6.4 Email Alert Module

- Sends email notifications for file integrity violations
- Notifies administrators immediately upon detection

---

## 7. Automation

The integrity checker script is automated using **cron**:

- Executes at fixed intervals
- Continuously monitors file integrity
- Runs without manual intervention

---

## 8. Security Considerations

- Credentials and API tokens are stored using environment variables
- Baseline file is protected from modification
- File integrity baseline is updated only after manual approval
- Prevents silent acceptance of unauthorized file changes

---

## 9. Results

The system successfully:

- Detected unauthorized modifications to monitored files
- Generated Jira tickets automatically
- Sent email alerts for detected integrity violations
- Operated automatically through scheduled execution

---

## 10. Limitations

- The system does not detect new file creation
- The system does not detect file deletion
- Monitoring is limited to files present in the baseline

---

## 11. Conclusion

This project demonstrates a practical implementation of a **File Integrity Monitoring system** using Python. By leveraging cryptographic hashing and automation, the system effectively detects file modifications and provides real-time alerts. The project aligns with fundamental security monitoring principles used in real-world environments.

---

## 12. Future Enhancements

- Detection of new and deleted files
- File whitelist and ignore rules
- Severity-based alert classification
- Integration with additional notification platforms

## 13. Screenshots
<img width="1920" height="923" alt="Screenshot_2026-01-02_23_40_48" src="https://github.com/user-attachments/assets/c8cd804a-cfe9-4935-8c13-3785b4749ffa" />

<img width="1920" height="923" alt="Screenshot_2026-01-02_23_41_13" src="https://github.com/user-attachments/assets/1bba6280-3e5e-4f29-b896-066b9b4e05cc" />
<img width="1920" height="923" alt="Screenshot_2026-01-02_23_40_58" src="https://github.com/user-attachments/assets/4d54451e-abc7-47c3-b21b-aeea4a7cbc23" />
<img width="1516" height="308" alt="Screenshot 2026-01-03 102012" src="https://github.com/user-attachments/assets/b2ac4d2a-399f-43af-b806-3982b37b5d58" />
<img width="1645" height="552" alt="Screenshot 2026-01-03 104040" src="https://github.com/user-attachments/assets/11b5ca52-f011-4b55-bada-7cd8443f14d5" />




