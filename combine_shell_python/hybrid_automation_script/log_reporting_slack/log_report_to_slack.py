import re
import requests

# Slack Webhook
WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"

# Log file path
LOG_FILE = "app.log"

# Initialize counters
info_count = 0
warning_count = 0
error_count = 0

# Store lines (optional: can include recent 5 errors/warnings)
errors = []
warnings = []

# Read and parse log file
with open(LOG_FILE, "r") as file:
    for line in file:
        if "[INFO]" in line:
            info_count += 1
        elif "[WARNING]" in line:
            warning_count += 1
            warnings.append(line.strip())
        elif "[ERROR]" in line:
            error_count += 1
            errors.append(line.strip())

# Create summary table (Slack supports Markdown)
summary = (
    "*📋 Log Report Summary:*\n\n"
    "```\n"
    "Log Level     | Count\n"
    "----------------------\n"
    f"INFO          | {info_count}\n"
    f"WARNING       | {warning_count}\n"
    f"ERROR         | {error_count}\n"
    "```\n"
)

# Add latest errors and warnings if available
if warnings:
    summary += "*⚠️ Latest Warnings:*\n```" + "\n".join(warnings[-3:]) + "```\n"
if errors:
    summary += "*❌ Latest Errors:*\n```" + "\n".join(errors[-3:]) + "```\n"

# Send to Slack
response = requests.post(WEBHOOK_URL, json={"text": summary})

# Confirm result
if response.status_code == 200:
    print("✅ Log report sent to Slack!")
else:
    print("❌ Failed to send Slack message.")
    print(response.text)
