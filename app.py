from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "data/kzon_univ.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "KZON Railway Backend OK"

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE user_id=? AND password=?",
        (data["id"], data["pw"])
    ).fetchone()

    if not user:
        return jsonify({"ok": False}), 401

    return jsonify({"ok": True, "role": user["role"]})

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
