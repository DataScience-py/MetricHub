def test_simple(client):
    assert client.get("/").status_code == 200
