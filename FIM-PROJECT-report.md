# File Integrity Monitoring System

## 1. Abstract

File Integrity Monitoring (FIM) is a critical security mechanism used to detect unauthorized modifications to files and directories. This project presents the design and implementation of a **Python-based File Integrity Monitoring system** that detects file integrity violations using cryptographic hashing and file metadata analysis. The system also supports detection of new and deleted files, automated incident ticket creation using **Atlassian Jira**, email alerting, and scheduled execution using Linux cron jobs. The project demonstrates practical security monitoring techniques used in real-world systems and emphasizes automation, secure configuration, and error handling.

---

## 2. Introduction

In modern computing environments, files play a crucial role in system configuration, application execution, and data storage. Unauthorized modification of files can lead to security breaches, malware execution, or system instability. File Integrity Monitoring is a security technique used to ensure that files remain unchanged unless explicitly authorized.

This project aims to build a lightweight but effective File Integrity Monitoring system using Python that can detect file modifications, additions, and deletions, and automatically report these incidents through a ticketing and alerting mechanism.

---

## 3. Objectives

The objectives of this project are:

- To monitor files within a specified directory
- To calculate cryptographic hash values for file integrity verification
- To detect unauthorized file modifications
- To detect new file creation and file deletion
- To generate automated incident tickets using Jira
- To send real-time email alerts for detected violations
- To automate the monitoring process using Linux scheduling
- To handle runtime errors and exceptions gracefully

---

## 4. Scope of the Project

The scope of this project includes:

- Monitoring of files inside a predefined directory
- Scheduled integrity checks at fixed intervals
- Automated alerting and incident creation

The project does not include:

- Kernel-level monitoring
- Real-time event-based monitoring
- Malware detection or prevention

---

## 5. System Architecture

The system follows a baseline-based monitoring approach and consists of the following components:

1. **Baseline Generator**
    
    Creates a trusted baseline of file hashes and metadata.
    
2. **Integrity Checker**
    
    Periodically scans monitored files and compares them with the baseline.
    
3. **Alerting Module**
    
    Sends email notifications and creates Jira tickets when violations are detected.
    
4. **Automation Layer**
    
    Uses cron jobs to execute the monitoring process automatically.
    

---

## 6. Technologies Used

- **Programming Language:** Python 3
- **Hashing Algorithm:** SHA-256
- **Operating System:** Linux
- **Ticketing System:** Jira REST API
- **Alerting Mechanism:** SMTP Email
- **Data Storage:** JSON
- **Automation Tool:** Cron

---

## 7. Project Directory Structure

```
fim/
│
├── baseline_generator.py
├── integrity_checker.py
├── jira_integration.py
├── email_alert.py
├── requirements.txt
│
├── monitor_folder/
│   └── app.py
│
└──data/
    └── baseline.json

```

---

## 8. Module Description

### 8.1 Baseline Generator

The baseline generator calculates the SHA-256 hash, last modified time, and change time of each monitored file. This information is stored in a JSON file and represents the trusted state of the system.

---

### 8.2 Integrity Checker

The integrity checker performs the following operations:

- Loads baseline data
- Scans current files
- Compares current hashes and metadata with baseline values
- Detects file modifications, new files, and deleted files
- Triggers alerts when violations are found

---

### 8.3 Jira Integration Module

This module integrates with Jira using REST APIs. When an integrity violation occurs, a new issue is automatically created in the Jira project, ensuring proper incident tracking and accountability.

---

### 8.4 Email Alert Module

The email alert module sends notification emails containing:

- File path
- Type of integrity violation
- Timestamp of detection

This provides immediate visibility of security incidents.

---

## 9. Automation Using Cron

The integrity checker is automated using Linux cron jobs and is scheduled to run **every one hour**. A wrapper shell script is used to load environment variables and execute the Python script reliably.

---

## 10. Security Considerations

- Sensitive credentials are stored using Linux environment variables
- Baseline generation is a manual and controlled operation
- No credentials are hardcoded in the source code
- Monitoring scripts are separated from monitored files to prevent false alerts

---

## 11. Error and Exception Handling

The project includes structured error handling for:

- File access and permission errors
- Missing or corrupted baseline files
- Network and Jira API failures
- Email transmission errors

This ensures that failures in one component do not crash the entire monitoring system.

---

## 12. Limitations

- The system performs scheduled monitoring, not real-time detection
- Very short-lived file changes may not be detected if reverted before the next scan
- Timestamp manipulation by privileged attackers is not prevented

---

## 13. Results

The system successfully:

- Detected file modifications
- Detected new file creation
- Detected file deletion
- Created Jira tickets automatically
- Sent email alerts with timestamps
- Ran autonomously using cron jobs

---

## 14. Future Enhancements

- Integration of real-time monitoring using Linux inotify
- Severity-based ticket prioritization
- Centralized logging and dashboards
- Integration with messaging platforms such as Slack or Teams

---

## 15. Conclusion

This project demonstrates the practical implementation of a File Integrity Monitoring system using Python. By combining cryptographic hashing, metadata analysis, automated alerting, and ticket creation, the system provides a reliable and extensible approach to file integrity monitoring. The project reflects real-world security monitoring practices and highlights the importance of automation and secure configuration in system security.

---

## References

- Linux File Integrity Monitoring Concepts
- Python Documentation
- Jira REST API Documentation

## 13. Screenshots
<img width="1920" height="923" alt="Screenshot_2026-01-02_23_40_48" src="https://github.com/user-attachments/assets/c8cd804a-cfe9-4935-8c13-3785b4749ffa" />

<img width="1920" height="923" alt="Screenshot_2026-01-02_23_41_13" src="https://github.com/user-attachments/assets/1bba6280-3e5e-4f29-b896-066b9b4e05cc" />
<img width="1920" height="923" alt="Screenshot_2026-01-02_23_40_58" src="https://github.com/user-attachments/assets/4d54451e-abc7-47c3-b21b-aeea4a7cbc23" />
<img width="1516" height="308" alt="Screenshot 2026-01-03 102012" src="https://github.com/user-attachments/assets/b2ac4d2a-399f-43af-b806-3982b37b5d58" />
<img width="1645" height="552" alt="Screenshot 2026-01-03 104040" src="https://github.com/user-attachments/assets/11b5ca52-f011-4b55-bada-7cd8443f14d5" />




