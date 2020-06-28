import pytest


def test_health(app, client):
    res = client.get('/')
    assert res.status_code == 200


@pytest.mark.parametrize('request_qty', [1, 10, 20, 50])
def test_uniq_responses(app, client, request_qty):
    responses = set()
    for request in range(request_qty):
        res = client.get('/')
        responses.add(res.data)
    assert len(responses) == request_qty
