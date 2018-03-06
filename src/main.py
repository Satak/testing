"""Test application"""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def root():
    """Main."""

    message = {
        "title": "This is a test flask application",
        "version": "1.4",
        "changes": [
            "1.4: fix",
            "1.3: deploy",
            "1.2: cached builder for faster build time",
            "1.1: message changed",
            "1.0: init commit"
        ]
    }

    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
