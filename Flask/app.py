from flask import Flask, jsonify, request
import threading
import time
import requests
import os
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, KHU-MCL!'

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message', '')
    response = {'response': f'Received: {message}'}
    app.logger.info(f'Received message: {message}')
    return jsonify(response)

def run_server():
    port = int(os.getenv('FLASK_PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def send_message():
    time.sleep(5)  # Give the server time to start
    server_host = os.getenv('SERVER_HOST', 'localhost')
    server_port = os.getenv('FLASK_PORT', 5000)
    url = f'http://{server_host}:{server_port}/api/message'
    payload = {'message': os.getenv('CLIENT_MESSAGE', 'Hello from the client!')}
    user = os.getenv('USER', 'Client') # Get the USER env, default to 'Client'
    app.logger.info(f'{user}: Sending message to Flask server')
    response = requests.post(url, json=payload)

if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Run the server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Run the client after a short delay
    send_message()
    
    # Keep the main thread alive to ensure the server keeps running
    while True:
        time.sleep(1)
