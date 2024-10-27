from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/get_pod_id', methods=['GET'])
def get_pod_id():
    pod_id = socket.gethostname()
    return f"<html><body><h1>Pod ID: {pod_id}</h1></body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
