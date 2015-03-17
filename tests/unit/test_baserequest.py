import pytest

from mock import patch, MagicMock, PropertyMock
from contextlib import nested


class MockResponse(object):
    status_code = 200

    def json(self):
        return dict(status_code=200, result=dict(foo='bar'))


@patch('cloudelementssdk.requests.get')
def test_base_class_can_use_methods(mock_get):
    from cloudelementssdk import BaseRequest
    with patch('cloudelementssdk.requests.Response') as mock_response:
        mock_response = MockResponse()
        mock_get.return_value = mock_response
        req = BaseRequest()
        req.base_url = 'http://www.foo.com/'
        response = req._get('/', params=dict(foo='bar'))
        assert response.status_code == 200
        assert response.json() == dict(status_code=200, result=dict(foo='bar'))


@patch('cloudelementssdk.requests.post')
def test_base_class_can_use_post(mock_get):
    from cloudelementssdk import BaseRequest
    with patch('cloudelementssdk.requests.Response') as mock_response:
        mock_response = MockResponse()
        mock_get.return_value = mock_response
        req = BaseRequest()
        req.base_url = 'http://www.foo.com/'
        response = req._post('/', data=[])
        assert response.status_code == 200
        assert response.json() == dict(status_code=200, result=dict(foo='bar'))


@patch('cloudelementssdk.requests.delete')
def test_base_class_can_use_delete(mock_get):
    from cloudelementssdk import BaseRequest
    with patch('cloudelementssdk.requests.Response') as mock_response:
        mock_response = MockResponse()
        mock_get.return_value = mock_response
        req = BaseRequest()
        req.base_url = 'http://www.foo.com/'
        response = req._delete('/')
        assert response.status_code == 200
        assert response.json() == dict(status_code=200, result=dict(foo='bar'))

@patch('cloudelementssdk.requests.put')
def test_base_class_can_use_put(mock_get):
    from cloudelementssdk import BaseRequest
    with patch('cloudelementssdk.requests.Response') as mock_response:
        mock_response = MockResponse()
        mock_get.return_value = mock_response
        req = BaseRequest()
        req.base_url = 'http://www.foo.com/'
        response = req._put('/', data=[])
        assert response.status_code == 200
        assert response.json() == dict(status_code=200, result=dict(foo='bar'))
