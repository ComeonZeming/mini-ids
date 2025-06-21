import json
from datetime import datetime
import os

# Paths
log_file = "../logs/sample_access.log"
rules_file = "../rules/attack_patterns.json"
alert_file = "../alerts/alerts.log"

# Load attack patterns
with open(rules_file, "r") as rf:
    patterns = json.load(rf)

# Read log entries
if not os.path.exists(log_file):
    print(f"[ERROR] Log file not found: {log_file}")
    exit(1)

with open(log_file, "r") as lf:
    lines = lf.readlines()

alerts = []
for line in lines:
    for pattern in patterns["rules"]:
        if pattern["match"] in line:
            alerts.append(f"[ALERT] {pattern['type']} detected: {line.strip()}")

# Write alerts
with open(alert_file, "a") as af:
    for alert in alerts:
        af.write(f"{datetime.now()} - {alert}\n")
        print(alert)
 
