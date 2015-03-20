import pytest
import unittest

from mock import patch, MagicMock, PropertyMock
from contextlib import nested

import httpretty


class TestCloudElements(unittest.TestCase):
    def setUp(self):
        from cloudelementssdk import CloudElements
        self.cloud_elements = CloudElements(
            user_secret='',
            org_secret=''
        )

    @httpretty.activate
    def test_get_accounts(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/accounts',
            body=json.dumps({'foo': 1})
        )

        resp = self.cloud_elements.get_accounts('where id=1')
        assert resp.json() == {'foo': 1}

    @httpretty.activate
    def test_create_accounts(self):
        import json
        httpretty.register_uri(
            httpretty.POST,
            self.cloud_elements.base_url + '/accounts',
            body=json.dumps({'foo': 1})
        )

        resp = self.cloud_elements.create_accounts({'Name': 'Gangta G Funk'})
        assert resp.json() == {'foo': 1}

    @httpretty.activate
    def test_get_account_by_id(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/accounts/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.get_account_by_id(acct_id=1)
        assert resp.json() == {'foo': 1}

    @httpretty.activate
    def test_update_account_by_id(self):
        import json
        httpretty.register_uri(
            httpretty.PATCH,
            self.cloud_elements.base_url + '/accounts/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements. \
            update_account_by_id(acct_id=1, data={'Name': 'Mario'})
        assert resp.json() == {'foo': 1}

    @httpretty.activate
    def test_delete_account_by_id(self):
        import json
        httpretty.register_uri(
            httpretty.DELETE,
            self.cloud_elements.base_url + '/accounts/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.delete_account_by_id(acct_id=1)
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.DELETE

    def test_bulk_query(self):
        pass

    def test_get_bulk_job_status(self):
        pass

    def test_get_bulk_job_object(self):
        pass

    def test_uploadbulk(self):
        pass

    @httpretty.activate
    def test_get_contacts(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/contacts',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.get_contacts(query="where id=1")
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.GET

    @httpretty.activate
    def test_create_contact(self):
        import json
        httpretty.register_uri(
            httpretty.POST,
            self.cloud_elements.base_url + '/contacts',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.create_contact({'LastName': 'foo'})
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.POST

    @httpretty.activate
    def test_delete_contact(self):
        import json
        httpretty.register_uri(
            httpretty.DELETE,
            self.cloud_elements.base_url + '/contacts/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.delete_contact(1)
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.DELETE

    @httpretty.activate
    def test_get_leads(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/leads',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.get_leads(query='where id=1')
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.GET

    @httpretty.activate
    def test_create_lead(self):
        import json
        httpretty.register_uri(
            httpretty.POST,
            self.cloud_elements.base_url + '/leads',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.create_lead({'LastName': 'foo'})
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.POST

    @httpretty.activate
    def test_get_lead(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/leads/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.get_lead(1)
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.GET

    @httpretty.activate
    def test_update_lead(self):
        import json
        httpretty.register_uri(
            httpretty.PATCH,
            self.cloud_elements.base_url + '/leads/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.update_lead(1, {'LastName': 'foo'})
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.PATCH

    @httpretty.activate
    def test_delete_lead(self):
        import json
        httpretty.register_uri(
            httpretty.DELETE,
            self.cloud_elements.base_url + '/leads/1',
            body=json.dumps({'foo': 1})
        )
        resp = self.cloud_elements.delete_lead(1)
        assert resp.json() == {'foo': 1}
        assert httpretty.last_request().method == httpretty.DELETE

    @httpretty.activate
    def test_get_sales_force_provision_url(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/elements/%s/oauth/url' % 'sfdc',
            body=json.dumps(dict(foo='bar'))
        )
        resp =  self.cloud_elements.get_sales_force_provision_url(
            key='foo',
            secret='bar',
            callback_url='http://test.com'
        )
        assert resp.status_code == 200
        assert resp.json() == dict(foo='bar')

    @httpretty.activate
    def test_provision_instance(self):
        import json
        httpretty.register_uri(
            httpretty.GET,
            self.cloud_elements.base_url + '/instances',
            body=json.dumps(dict(foo='bar'))
        )
        resp =  self.cloud_elements.get_sales_force_provision_url(
            key='foo',
            secret='bar',
            callback_url='http://test.com'
        )
        assert resp.status_code == 200
        assert resp.json() == dict(foo='bar')
