from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import logging
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Basic logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    logger.info('Hello World endpoint hit.')
    return 'Hello, DevOps Monitoring!'

@app.route('/error')
def error_endpoint():
    if random.random() < 0.7: # 70% chance of error
        logger.error('Simulating an internal server error (HTTP 500)')
        return 'Simulated Server Error', 500
    else:
        logger.info('Error endpoint hit, but no error this time.')
        return 'No error this time', 200

# ... other routes (e.g., /slow, /login with custom metrics)