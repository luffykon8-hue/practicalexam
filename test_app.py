from api import api
def test_home_status_code():
    tester = api.test_client()
    response = tester.get('/users')
    assert response.status_code == 200
    assert b"Hello this is the testing API for practical exam in test_app" in response.data
def test_home_content():
    tester = api.test_client()
    response = tester.get('/users')
    assert b"Hello this is the testing API for practical exam in test_app" in response.data
if __name__ == '__main__':
    api.run()
    test_home_status_code()
    test_home_content() 