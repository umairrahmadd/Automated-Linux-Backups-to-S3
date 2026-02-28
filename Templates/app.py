from flask import Flask, render_template, jsonify
import os, shutil, subprocess
from datetime import datetime

app = Flask(__name__)

# Base paths (safe defaults)
BASE_DIR = os.path.join(os.path.expanduser("~"), "backup_demo")
SRC_DIR = os.path.join(BASE_DIR, "project_data")
DEST_DIR = os.path.join(BASE_DIR, "local_backups")
LOG_FILE = os.path.join(BASE_DIR, "backup.log")

# --- Local Backup Function ---
def run_local_backup():
    if not os.path.isdir(SRC_DIR):
        return False, f"Source folder not found: {SRC_DIR}"

    os.makedirs(DEST_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest_path = os.path.join(DEST_DIR, f"backup_{timestamp}")

    try:
        shutil.copytree(SRC_DIR, dest_path)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Local backup created: {dest_path}\n")
        return True, f"Local backup created: {dest_path}"
    except Exception as e:
        return False, f"Backup failed: {e}"

# --- Upload to S3 Function ---
def upload_to_s3():
    bucket_name = "user-demo-backups-12345"   # replace with real bucket later
    region = "us-east-1"

    cmd = f'aws s3 sync "{DEST_DIR}" s3://{bucket_name}/ --delete --region {region}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    ok = (result.returncode == 0)
    output = result.stdout if ok else result.stderr
    return ok, output.strip() if output else ("Success" if ok else "Unknown error")

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/backup", methods=["POST"])
def backup():
    ok, msg = run_local_backup()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"ok": ok, "timestamp": timestamp, "output": msg})

@app.route("/log")
def log():
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        return jsonify({"ok": True, "log": content})
    return jsonify({"ok": False, "log": "Log file not found."})

@app.route("/upload", methods=["POST"])
def upload():
    ok, msg = upload_to_s3()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"ok": ok, "timestamp": timestamp, "output": msg})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
