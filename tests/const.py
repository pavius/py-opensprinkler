import os

URL = os.environ.get("CONTROLLER_URL") or "http://10.0.0.200:8080"
PASSWORD = os.environ.get("CONTROLLER_PASSWORD") or "Oz4pa3yt!"
FIRMWARE_VERSION = float(os.environ.get("CONTROLLER_FIRMWARE") or "219")
