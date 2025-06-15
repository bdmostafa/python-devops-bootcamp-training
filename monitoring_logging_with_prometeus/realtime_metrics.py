from flask import Flask, Response
from prometheus_client import start_http_server, Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

import time

app = Flask(__name__)

# Define custom metric
http_requests_total = Counter('http_requests_total', 'Total HTTP Requests')

# Define a histogram to measure request latency
request_latency = Histogram('request_latency_seconds', 'Request latency')


@app.route('/')
def index():
    http_requests_total.inc()
    return "Welcome to the monitored Flask app!"

@app.route('/slow')
def slow():
    http_requests_total.inc()
    time.sleep(2)  # simulate delay
    return "Slow route!"

@app.route('/work')
@request_latency.time()  # automatically measures function latency
def work():
    time.sleep(1.2)
    return "Work complete"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
