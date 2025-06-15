from flask import Flask, request, jsonify
import logging
import json
import requests # For sending to external services like Slack

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SLACK_WEBHOOK_URL = 'YOUR_SLACK_WEBHOOK_URL_HERE' # Replace with your Slack webhook following this documentation: https://api.slack.com/messaging/webhooks

def send_slack_notification(alert_data):
    if not SLACK_WEBHOOK_URL:
        logger.warning("Slack webhook URL not configured. Skipping Slack notification.")
        return

    for alert in alert_data.get('alerts', []):
        status = alert.get('status', 'unknown').upper()
        alertname = alert.get('labels', {}).get('alertname', 'N/A')
        instance = alert.get('labels', {}).get('instance', 'N/A')
        summary = alert.get('annotations', {}).get('summary', 'No summary.')

        message = {
            "text": f"*{status} Alert:* {alertname} on {instance}\nSummary: {summary}"
        }
        try:
            response = requests.post(SLACK_WEBHOOK_URL, json=message)
            response.raise_for_status()
            logger.info(f"Slack notification sent for alert: {alertname} ({status})")
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send Slack notification: {e}")

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.get_json()
    logger.info(f"Received alert from Alertmanager: {json.dumps(data, indent=2)}")
    send_slack_notification(data) # Send to Slack
    return jsonify({"status": "success", "message": "Alert received and processed"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)