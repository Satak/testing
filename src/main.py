"""Test application"""

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def root():
    message = {
        "message": "This is a test flask application"
    }

    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
