#!/bin/bash

while true; do
    echo "Running log generator..."
    python3 generate_log.py

    if [ -s app.log ]; then
        echo "Log file is not empty. Sending report to Slack..."
        python3 log_report_to_slack.py
    else
        echo "Log file is empty. Skipping report..."
    fi

    echo "Sleeping for 30 seconds..."
    sleep 30
done
