#!/bin/bash
set -e

APP_DIR="/opt/check-lock-web"
USER=$(logname)

echo "[*] Setting up Python virtual environment..."
python3 -m venv "$APP_DIR/venv"
"$APP_DIR/venv/bin/pip" install flask

echo "[*] Enabling systemd service..."
systemctl daemon-reload
systemctl enable "check-lock-web@${USER}.service"
systemctl start "check-lock-web@${USER}.service"

echo "[*] check-lock-web is now running at http://localhost:8080"
