from flask import Flask
import subprocess

app = Flask(__name__)

def is_locked():
    try:
        result = subprocess.run(
            "loginctl | grep $USER | awk '{print $1}' | head -n 1",
            shell=True, capture_output=True, text=True
        )
        session_id = result.stdout.strip()
        if not session_id:
            return None

        result = subprocess.run(
            f"loginctl show-session {session_id} -p LockedHint",
            shell=True, capture_output=True, text=True
        )
        return result.stdout.strip().endswith("yes")
    except Exception:
        return None

@app.route("/")
def index():
    locked = is_locked()
    if locked is None:
        state, color = "⚠️ Unknown", "gray"
    elif locked:
        state, color = "🔒 Locked", "red"
    else:
        state, color = "🔓 Unlocked", "green"

    return f"""
    <html>
      <head>
        <meta http-equiv="refresh" content="5">
        <style>
          body {{
            font-family: sans-serif;
            text-align: center;
            margin-top: 20%;
            font-size: 3em;
            color: {color};
          }}
        </style>
      </head>
      <body>{state}</body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
