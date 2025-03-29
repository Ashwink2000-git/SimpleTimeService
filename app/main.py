from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    # Get client IP (considering proxies)
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For'].split(',')[0]
    else:
        ip = request.remote_addr

    return jsonify({
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'ip': ip
    })

if __name__ == '__main__':
    # Run on port 8080 as non-root user would need
    app.run(host='0.0.0.0', port=8080)
