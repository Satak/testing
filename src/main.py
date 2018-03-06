"""Test application"""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def root():
    """Main."""

    message = {
        "title": "This is a test flask application",
        "version": "1.1",
        "changes": [
            "1.1: message changed",
            "1.0: init commit"
        ]
    }

    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
