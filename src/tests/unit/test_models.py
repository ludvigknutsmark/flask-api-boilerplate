from api.models import User

def test_create_user():
    user = User(username="test", password="testpw")
    assert user.username == "test"
    assert user.password == "testpw"