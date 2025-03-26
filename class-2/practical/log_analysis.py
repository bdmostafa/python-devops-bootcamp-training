# Automating Log File Analysis | Perse System Logs
# Problem: Large log files are hard to analyze manually.
# Solution: Use Python to scan logs, detect issues, and generate reports.

# Scan system logs and alert admins if errors are found.
import os

log_file = "/var/logs/sys.log"

with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line or "WARNING" in line:
            print(line.strip())  # Print only error logs
