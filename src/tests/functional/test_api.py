import json
from server import app

test_client = app.test_client()

def test_index():
    response = test_client.get("/")
    assert b"<p>Hello, Flask Boilerplate!</p>" in response.data

def test_get_user():
    response = test_client.get("/api/user/1")
    response_data = json.loads(response.data.decode("utf-8"))
    assert type(response_data) is dict
    assert len(response_data) == 1
    assert response_data.get("username") == "admin"
    # Check that password is not leaking in get_user
    assert "password" not in response_data
