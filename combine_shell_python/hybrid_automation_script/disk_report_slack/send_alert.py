# https://api.slack.com/messaging/webhooks

import sys
import requests

if len(sys.argv) < 2:
    print("Usage: python3 send_alert.py <disk_usage_percentage>")
    sys.exit(1)
    
usage = sys.argv[1]
webhook_url = "https://hooks.slack.com/services/your/webhook/url"

data = {
    "text": f"⚠️ Disk Usage Alert: Server usage is at {usage}%. Please take action."
}

res = requests.post(webhook_url, json=data)

if res.status_code == 200:
    print("Slack alert sent successfully.")
else:
    print("Failed to send alert.")
    print(f"Error: {res.status_code} - {res.text}")