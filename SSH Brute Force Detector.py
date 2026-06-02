import csv
import os
import random
from datetime import datetime

CSV_FILE = "ssh_logs.csv"
REPORT_FILE = "report.txt"

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "cyber123"

ips = ["192.168.1.55", "10.0.0.7", "172.16.1.25", "192.168.0.101", "203.0.113.45"]

IP_ADDRESS = random.choice(ips)

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "ip", "username", "status"])

def log_attempt(ip, username, status):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ip, username, status])

def count_failures(ip):
    failures = 0

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["ip"] == ip and row["status"] == "Failed":
                failures += 1

    return failures

def get_risk_level(attempts):
    if attempts >= 10:
        return "HIGH"
    elif attempts >= 5:
        return "MEDIUM"
    else:
        return "LOW"

def most_targeted_username():
    usernames = {}

    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["status"] == "Failed":
                username = row["username"]
                usernames[username] = usernames.get(username, 0) + 1

    if not usernames:
        return "None"

    return max(usernames, key=usernames.get)

def generate_report(ip, attempts, risk, username):
    with open(REPORT_FILE, "w") as report:
        report.write("SSH BRUTE FORCE DETECTION REPORT\n")
        report.write("=" * 35 + "\n\n")
        report.write(f"Suspicious IP: {ip}\n")
        report.write(f"Failed Attempts: {attempts}\n")
        report.write(f"Risk Level: {risk}\n")
        report.write(f"Most Targeted Username: {username}\n")
        report.write("\nPossible SSH Brute Force Attack Detected\n")

print()
print("SSH BRUTE FORCE LOG DETECTOR")
print()

print(f"\nIncoming Connection From: {IP_ADDRESS}")

while True:

    username = input("\nUsername: ")
    password = input("Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\nLogin Successful")
        log_attempt(IP_ADDRESS, username, "Success")
        break

    else:
        print("\nLogin Failed")

        log_attempt(IP_ADDRESS, username, "Failed")

        failures = count_failures(IP_ADDRESS)
        risk = get_risk_level(failures)

        print(f"Failed Attempts: {failures}")
        print(f"Risk Level: {risk}")

        if failures >= 5:
            targeted_user = most_targeted_username()

            print("SECURITY ALERT")
            print("Possible SSH Brute Force Attack Detected")
            print(f"Suspicious IP: {IP_ADDRESS}")

            generate_report(IP_ADDRESS, failures, risk, targeted_user)

            print("Report Generated Successfully")

print()
print("SESSION SUMMARY")
print()

total_failures = count_failures(IP_ADDRESS)

print(f"IP Address: {IP_ADDRESS}")
print(f"Total Failed Attempts: {total_failures}")
print(f"Risk Level: {get_risk_level(total_failures)}")
print(f"Most Targeted Username: {most_targeted_username()}")
print("\nLog File Saved As: ssh_logs.csv")
print("Report Saved As: report.txt")