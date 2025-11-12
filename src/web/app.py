import sys
import os

# Add the parent directory of 'web' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import threading
import redis
from flask import Flask
# from flask_cors import CORS
from flask import send_from_directory
from flask_socketio import SocketIO
import json
import time
import os
from Consumer.Consumer import consume_event


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")




@app.route("/")
def index():
    return send_from_directory(app.root_path, "index.html")

if __name__ == "__main__":
    threading.Thread(target=consume_event,args=(socketio,), daemon=True).start()
    socketio.run(app, host='0.0.0.0', port=5000)