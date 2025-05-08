#!/bin/bash

# Run the scrapper
# Assuming you have a Python script named booking_review_scrapper.py that scrapes booking reviews and saves them to a CSV file.
# Make sure to replace this with the actual path to your Python script
# and the CSV file it generates.
python3 booking_review_scrapper.py 


# File to be uploaded
# This script uploads a CSV file to a Slack channel using the Slack API.
# SLACK_TOKEN="xoxb-*************"
CHANNEL="#all-devops-test"  # or channel ID like C01234567
CSV_FILE="booking_reviews.csv"
WEBHOOK_URL="https://hooks.slack.com/services/webhook_url"

# Check if file exists
if [[ ! -f "$CSV_FILE" ]]; then
    echo "❌ File not found!"
    exit 1
fi

# # Upload CSV as a file to Slack
# curl -F file=@"$FILE" \
#      -F "initial_comment=📎 Here's the latest CSV data from scrapper" \
#      -F channels="$CHANNEL" \
#      -H "Authorization: Bearer $SLACK_TOKEN" \
#      https://slack.com/api/files.upload


# Check if file exists and is not empty
if [[ -s "$CSV_FILE" ]]; then
    curl -X POST -H 'Content-type: application/json' \
    --data "{
        \"text\": \"📊 CSV report is ready: *$CSV_FILE*\"
    }" $WEBHOOK_URL
else
    echo "❌ CSV file not found or empty."
fi