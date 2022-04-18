from src.drivers.http_requester import HttpRequester

def test_request_from_url(requests_mock):
    url = 'https://www.google.com'
    requests_mock.get(url, status_code=200, text='<html>Hello World!</html>')
    http_requester = HttpRequester(url)
    response = http_requester.request_from_url()

    assert 'status_code' in response
    assert 'html' in response
    assert response['status_code'] == 200
    assert response['html'] == '<html>Hello World!</html>'
