import requests


def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]
    assert "email" in data[0]
