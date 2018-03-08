"""Test application"""

from datetime import datetime

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

IN_PROD = False

DP_PATH = 'sqlite:////Dev/satak/testing/db/test.db'

if IN_PROD:
    DP_PATH = 'sqlite:////var/lib/sql/data/test.db'


app.config['SQLALCHEMY_DATABASE_URI'] = DP_PATH
db = SQLAlchemy(app)

class VersionHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String(80), nullable=False)
    change = db.Column(db.String(80), nullable=False)
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, version, change):
        self.version = version
        self.change = change

    def as_dict(self):
        return {
            "id": self.id,
            "version": self.version,
            "change": self.change,
            "date_time": self.date_time
        }

def changes_ctrl():
    return [item.as_dict() for item in VersionHistory.query.all()]

def message_ctrl():
    changes = changes_ctrl()
    return {
        "changes": changes,
        "time": "07.03.2018 09:22"
    }

@app.route("/init")
def init():
    db.create_all()
    return jsonify({"message": "DB Created"})

@app.route("/")
def root():
    """UI."""

    return render_template('index.html', data=message_ctrl())


@app.route("/api/changes", methods=['POST'])
def api_new_change():
    """Post new change."""

    change = VersionHistory(**request.get_json(silent=True))
    db.session.add(change)
    db.session.commit()
    return jsonify(change.as_dict()), 201

@app.route("/api/changes")
def api_changes():
    """Get vesion history."""

    return jsonify(changes_ctrl())

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
