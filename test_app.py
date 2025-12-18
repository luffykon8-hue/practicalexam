from app import app
def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hello this is the testing API for practical exam in test_app" in response.data

if __name__ == '__main__':
    app.run()
    test_home_status_code()
