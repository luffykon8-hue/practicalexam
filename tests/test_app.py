from app import app

def test_home_status_code():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello! This is a simple Flask application running inside Docker.NoYaaaaaaa" in resp.data
