"""Test application"""

from flask import Flask, jsonify, render_template

app = Flask(__name__)

def message_ctrl():
    return {
        "title": "This is a test flask application.",
        "version": "1.96",
        "changes": [
            {"1.96": "minor tweaks"},
            {"1.9": "multi namespace"},
            {"1.8": "morning change"},
            {"1.7": "html template added"},
            {"1.6": "tag name added to cloudbuild.yaml"},
            {"1.5": "time changed"},
            {"1.0": "init commit"}
        ],
        "status": "staging",
        "time": "07.03.2018 14:28"
    }

@app.route("/")
def root():
    """UI."""

    return render_template('index.html', data=message_ctrl())

@app.route("/api/version")
def api_version():
    """Api version."""

    return jsonify(message_ctrl())

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
