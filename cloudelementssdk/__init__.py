import logging
import json
import requests
import time
import os

from requests.exceptions import *

log = logging.getLogger(__name__)


def _log_info(path, status, data, request_type, headers, chrono,  exception=None):

    if exception:
        log.error(
            "[CloudElements] \
             path=%(url)s \
             http_status=%(http_status)s \
             error=%(error)s \
             request_type=%(request_type)s \
             post=%(post)s \
             ms=%(ms).0f", {
                "url": path,
                "http_status": status,
                "error": exception,
                "post": data,
                "ms": chrono,
                "request_type": request_type
            }
        )

    else:
        log.info(
            "[CloudElements] \
             path=%(url)s \
             http_status=%(http_status)s \
             request_type=%(request_type)s \
             post=%(post)s \
             ms=%(ms).0f", {
                "url": path,
                "http_status": status,
                "post": data,
                "ms": chrono,
                "request_type": request_type
            }
        )


class BaseRequest(object):
    """ BaseRequest Object for Resources
    """
    base_url = ''
    headers = {
        "Content-type": "application/json",
        "Accept":  "application/json",
        "Connection": "close",
    }

    def __init__(self, base_url=None):
        """ Initialization function for BaseRequest """
        self.base_url = base_url or self.base_url

    def _send_request(self, url, method='GET', **kwargs):
        """ Base send method for request """
        headers = kwargs.get('headers', None)
        params = kwargs.get('params', None)
        data = kwargs.get('data', None)
        auth_token = kwargs.get('auth_token')
        url = '%s%s' % (self.base_url, url)

        if auth_token:
            headers['Authorization'] = auth_token

        exception = None
        chrono = time.time()
        status = None

        try:
            method = method.upper()
            response = None
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(
                    url=url,
                    data=data,
                    headers=headers
                )
            elif method == 'DELETE':
                response = requests.delete(
                    url=url,
                    params=params,
                    headers=headers
                )
            elif method == 'PUT':
                response = requests.put(
                    url=url,
                    params=params,
                    headers=headers,
                    data=data
                )

            status = response.status_code

            return response
        except Exception as exc:
            exception = exc

        chrono = (time.time() - chrono) * 1000  # ms
        _log_info(
                path=url,
                status=status,
                data=data or None,
                request_type=method,
                headers=headers,
                chrono=chrono,
                exception=exception
            )

    def _post(self, url, data, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers' , self.headers)

        return self._send_request(
            url=url,
            data=data,
            method='POST',
            headers=headers,
            params=params
        )

    def _get(self, url, params=None, **kwargs):
        headers = kwargs.get('headers')

        return self._send_request(
            url=url,
            method='GET',
            params=params,
            headers=headers
        )

    def _put(self, url, data, **kwargs):
        headers = kwargs.get('headers', self.headers)
        params = kwargs.get('params')

        return self._send_request(
            url=url,
            method='PUT',
            data=data,
            params=params,
            headers=headers
        )

    def _delete(self, url, **kwargs):
        headers = kwargs.get('headers', self.headers)
        params = kwargs.get('params')

        return self._send_request(
            url=url,
            method='DELETE',
            params=params,
            headers=headers
        )


class CloudElements(BaseRequest):
        base_url = 'https://console.cloud-elements.com/elements/api-v2'


"""
Response Messages
HTTP Status Code    Reason  Response Model
200 OK - Everything worked as expected
400 Bad Request - Often due to a missing request parameter
401 Unauthorized - An invalid element token, user secret and/or org secret provided
403 Forbidden - Access to the resource by the provider is forbidden
404 Not found - The requested resource is not found
405 Method not allowed - Incorrect HTTP verb used, e.g., GET used when POST expected
406 Not acceptable - The response content type does not match the "Accept" header value
409 Conflict - If a resource being created already exists
415 Unsupported media type - The server cannot handle the requested Content-Type
500 Server error - Something went wrong on the Cloud Elements server
502 Provider server error - Something went wrong on the Provider or Endpoint's server
"""
