import logging
import json
import requests
import time
import os

from requests.exceptions import *

from cloudelementssdk.schemas.jsonschemas import *
from cloudelementssdk.validation import validate_schema

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
        headers = kwargs.get('headers', {})
        params = kwargs.get('params', None)
        data = kwargs.get('data', None)
        auth_token = kwargs.get('auth_token')
        url = '%s%s' % (self.base_url, url)

        if auth_token:
            headers['Authorization'] = auth_token

        exception = None
        chrono = time.time()
        status = None
        response = None

        try:
            method = method.upper()
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
            elif method == 'PATCH':
                response = requests.patch(
                    url=url,
                    params=params,
                    headers=headers,
                    data=data
                )
            else:
                raise Exception("Method not found.")

            status = response.status_code

            if response.status_code >= 400:
                response.raise_for_status()

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

        return response

    def _post(self, url, data, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers' , self.headers)

        return self._send_request(
            url=url,
            data=data,
            method='POST',
            headers=headers,
            params=params,
            **kwargs
        )

    def _get(self, url, params=None, **kwargs):
        headers = kwargs.get('headers', {})

        return self._send_request(
            url=url,
            method='GET',
            params=params,
            headers=headers,
            **kwargs
        )

    def _put(self, url, data, **kwargs):
        headers = kwargs.get('headers', self.headers)
        params = kwargs.get('params')

        return self._send_request(
            url=url,
            method='PUT',
            data=data,
            params=params,
            headers=headers,
            **kwargs
        )

    def _patch(self, url, data, **kwargs):
        headers = kwargs.get('headers', self.headers)
        params = kwargs.get('params')

        return self._send_request(
            url=url,
            method='PATCH',
            data=data,
            params=params,
            headers=headers,
            **kwargs
        )

    def _delete(self, url, **kwargs):
        headers = kwargs.get('headers', {})
        params = kwargs.get('params')

        return self._send_request(
            url=url,
            method='DELETE',
            params=params,
            headers=headers,
            **kwargs
        )


class CloudElements(BaseRequest):
        base_url = 'https://console.cloud-elements.com/elements/api-v2'
        auth_token = ''

        def __init__(self, auth_token):
            super(BaseRequest, self).__init__
            self.auth_token = auth_token
            self.headers['Authorization'] = auth_token

        def get_accounts(self,  query):
            """ /accounts GET """
            pass

        def create_accounts(self, data):
            """ /accounts POST """
            pass

        def get_account_by_id(self, acct_id):
            """ /accounts/{id} GET """
            pass

        def update_account_by_id(self, acct_id, data):
            """ /accounts/{id} PATCH """
            pass

        def delete_account_by_id(self, acct_id):
            """ /accounts/{id} DELETE """
            pass

        def bulk_query():
            """ /bulk/query GET """
            pass

        def get_bulk_job_status(self, jobid):
            """ /bulk/{id}/status GET """
            pass

        def get_bulk_job_errors(self, jobid):
            """ /bulk/{id}/errors GET """
            pass

        def get_bulk_job_object(self, jobid, object_name):
            """ /bulk/{id}/{object_name} GET """
            pass

        def upload_bulk(self, object_name, data):
            """
                /bulk/{object_name} POST
                Bulk upload of file objects to object_name
            """
            pass

        def create_contact(self, data):
            """ /contacts POST """
            pass

        def get_contact(self, contact_id):
            """ /contacts/{id} GET """
            pass

        def get_contacts(self, query):
            """ /contacts GET """
            pass

        def update_contact(self, contact_id, data):
            """ /contacts/{id} PATCH """
            pass

        def delete_contact(self, contact_id):
            """ /contacts/{id} DELETE """
            pass

        def get_leads(self, query):
            """ /leads GET """
            pass

        def create_lead(self, data):
            """ /leads POST """

            pass

        def get_lead(self, id):
            """ /leads/{id} GET """
            pass

        def update_lead(self, lead_id, data):
            """ /leads/{id} PATCH """
            pass

        def delete_lead(self, id):
            """ /leads/{id} DELETE """
            pass

        #TODO opportunities, objects, users

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
