# SSH-brute-force-detector


A command-line tool that simulates SSH login attempts, logs authentication activity, and detects potential brute-force attacks through CSV log analysis.

Built with Python using file handling, CSV logging, and basic security monitoring concepts.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Category](https://img.shields.io/badge/category-Cybersecurity-green)

---

## Features

* Simulate SSH login attempts
* Automatically create and maintain authentication logs
* Log successful and failed login attempts to CSV
* Detect suspicious login activity based on failed attempt thresholds
* Assign attack risk levels (Low, Medium, High)
* Identify the most targeted username
* Generate incident reports for detected brute-force attacks
* Simulate multiple attackers using randomized IP addresses

---

## Requirements

```bash
python 3.x
```

No external libraries are required.

## Usage

```bash
python ssh_detector.py
```

```text
========================================
SSH BRUTE FORCE LOG DETECTOR
========================================

Incoming Connection From: 192.168.1.55

Username:
Password:
```

---

## How it works

1. A simulated attacker attempts to log in using a username and password
2. Each login attempt is recorded in `ssh_logs.csv`
3. Failed login attempts are counted for each IP address
4. Risk levels are assigned based on the number of failures
5. If the threshold is exceeded, the system raises an alert
6. A security report is generated and saved to `report.txt`

---

## Example Log Entry

```csv
timestamp,ip,username,status
2026-06-02 14:22:01,192.168.1.55,admin,Failed
```

---

## Project Structure

```text
SSH-Bruteforce-Detector/

├── ssh_detector.py
├── ssh_logs.csv
└── report.txt
```

---

## Learning Outcomes

* Python file handling
* CSV processing
* Authentication logging
* Brute-force attack detection
* Security monitoring concepts
* Basic SOC analyst workflows

---

## ⚠️ Important

* This project is intended for educational purposes and security awareness training.
* It simulates attack detection and does not perform any real brute-force activity.
