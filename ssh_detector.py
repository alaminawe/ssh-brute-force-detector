import re
import subprocess
import collections

LOGFILE = "/var/log/auth.log"
THRESHOLD = 5

def detect_attacks():
    with open(LOGFILE, "r") as f:
        logs = f.readlines()
    failed_attempts = collections.Counter()
    for line in logs:
        if "Failed password" in line:
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1
    for ip, count in failed_attempts.items():
        if count >= THRESHOLD:
            print(f"[ALERT] {ip} has {count} failed login attempts - BLOCKING")
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
            print(f"[BLOCKED] {ip} has been blocked successfully")

detect_attacks()
