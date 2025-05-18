from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Secure World!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/secret')
def secret():
    return os.popen('cat /etc/passwd').read()
