# !/bin/bash

usage=$(df -h / | grep -v Filesystem | awk '{print $5}' | sed 's/%//')

if [ "$usage" -gt 80 ]; then
    echo "Disk usage is high: $usage%"
    python3 send_alert.py "$usage"
else
    echo "Disk usage is normal: $usage%"
fi