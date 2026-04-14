def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_user_email_format(api_client):
    response = api_client.get("/users")

    data = response.json()

    for user in data:
        assert "@" in user["email"]
