from api.schemas import UserSchema, user_schema

def test_user_schema():
    # create a user instance
    user = {
        "id": 1,
        "username": "testuser",
        "password": "password"
    }
    
    schema = UserSchema()

    # check that the password field is marked as dump_only
    assert schema.fields["id"].load_only == True
    assert schema.fields["password"].load_only == True

    # serialize the user instance
    result = user_schema.dump(user)

    # check that the password field is not included in the serialized data
    assert "id" not in result
    assert "password" not in result
    
    assert result["username"] == "testuser"