import subprocess
import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"

result = subprocess.run(["bandit", "-r", "app/"], capture_output=True, text=True)
output = result.stdout

print(output)

# Check for high severity issues
if "HIGH" in output:
    requests.post(SLACK_WEBHOOK_URL, json={"text": "🚨 Bandit found HIGH severity issues!"})
    # requests.post(SLACK_WEBHOOK_URL, json={"text": "🚨 Bandit found HIGH severity issues!"}, timeout=10)
