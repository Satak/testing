"""Test application"""

from os import environ
from flask import Flask, jsonify
app = Flask(__name__)

TAG = environ.get('TAG')

@app.route("/")
def root():
    """Main."""

    message = {
        "title": "This is a test flask application.",
        "version": "1.9",
        "tag": TAG,
        "changes": [
            "1.9: tag name added to cloudbuild.yaml",
            "1.8: time changed",
            "1.7: status added",
            "1.6: revision id",
            "1.5: after init deployment",
            "1.4: fix",
            "1.3: deploy",
            "1.2: cached builder for faster build time",
            "1.1: message changed",
            "1.0: init commit"
        ],
        "status": "production",
        "time": "06.03.2018 23:56"
    }

    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
