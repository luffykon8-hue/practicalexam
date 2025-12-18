import subprocess
import sys
import time

import requests


def _start_app():
    # start the app as a background process
    return subprocess.Popen([sys.executable, "loop.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def _wait_for(url, timeout=10):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=1)
            return r
        except requests.exceptions.RequestException:
            time.sleep(0.5)
    raise RuntimeError(f"Service did not become available at {url} within {timeout}s")


def test_home_connectivity():
    proc = _start_app()
    try:
        r = _wait_for("http://127.0.0.1:5000/", timeout=12)
        assert r.status_code == 200
        assert "Hello Flask" in r.text
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
