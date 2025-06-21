# Mini Log-Based Intrusion Detection System (Mini IDS)

This is a simple Python-based intrusion detection system that scans web server access logs and detects suspicious patterns such as admin page scans or file access violations.

## 🔍 What It Does

- Parses server logs (`sample_access.log`)
- Uses rules from `attack_patterns.json`
- Flags suspicious activities (e.g., `/admin`, `/etc/passwd`)
- Writes alerts to console and `alerts.log`

## 📂 Project Structure

mini-ids/
├── alerts/ # Output alerts go here
├── logs/ # Input access logs
├── rules/ # JSON file of patterns
├── src/ # Python detection script
├── README.md
└── requirements.txt 

## ▶️ How to Run

```bash
cd src
python detect_intrusion.py
```

## 📜 Example Alert
[ALERT] Admin Panel Scan detected: 192.168.1.50 - - [21/Jun/2025:13:55:36] "GET /admin" 404

## 🧠 Skills Demonstrated

- Pattern matchi

- File I/O in Python
