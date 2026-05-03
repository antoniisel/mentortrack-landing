import json
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")

LEAD_SINK = Path(os.environ.get("LEAD_SINK", "leads.json"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/lead", methods=["POST"])
def lead():
    data = request.get_json(silent=True) or request.form.to_dict()
    email = (data.get("email") or "").strip()
    if not email or "@" not in email:
        return jsonify({"ok": False, "error": "invalid_email"}), 400

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "email": email,
        "plan": data.get("plan"),
        "source": data.get("source"),
    }

    leads = []
    if LEAD_SINK.exists():
        try:
            leads = json.loads(LEAD_SINK.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            leads = []
    leads.append(record)
    LEAD_SINK.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

    return jsonify({"ok": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")
