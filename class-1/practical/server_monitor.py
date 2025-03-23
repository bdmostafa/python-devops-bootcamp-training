import os
import psutil  # To fetch system resource usage
import logging
import sys
from datetime import datetime

# Setup Logging
LOG_FILE = "server_health.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to check system health
def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu": cpu_usage,
        "memory": memory.percent,
        "disk": disk.percent
    }

# Lambda function for alert message
alert_message = lambda metric, value: f"ALERT! High {metric} usage detected: {value}%"

# Main monitoring function
def monitor_server(thresholds):
    logging.info("Starting server health monitoring...")
    while True:
        try:
            health = check_system_health()
            print(f"CPU: {health['cpu']}%, Memory: {health['memory']}%, Disk: {health['disk']}%")
            logging.info(f"CPU: {health['cpu']}%, Memory: {health['memory']}%, Disk: {health['disk']}%")

            # Check thresholds
            if health['cpu'] > thresholds['cpu']:
                logging.warning(alert_message("CPU", health['cpu']))
            if health['memory'] > thresholds['memory']:
                logging.warning(alert_message("Memory", health['memory']))
            if health['disk'] > thresholds['disk']:
                logging.warning(alert_message("Disk", health['disk']))

        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")
            sys.exit(1)  # Exit on error

# Default threshold values
thresholds = {
    "cpu": int(os.getenv("CPU_THRESHOLD", 80)),  # Fetch from environment or use default 80%
    "memory": int(os.getenv("MEMORY_THRESHOLD", 80)),
    "disk": int(os.getenv("DISK_THRESHOLD", 90))
}

# Run the monitoring function
monitor_server(thresholds)
