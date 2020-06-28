def test_health(app, client):
    res = client.get('/')
    assert res.status_code == 200
