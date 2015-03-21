import pytest
import unittest

from mock import patch, MagicMock, PropertyMock
from contextlib import nested


class TestCloudElements(unittest.TestCase):
    def setUp(self):
        import os
        from cloudelementssdk import CloudElements

        self.user_secret = os.getenv('CLOUD_ELEMENTS_USER_SECRET')
        self.org_secret = os.getenv('CLOUD_ELEMENTS_ORG_SECRET')
        self.sales_force_secret = os.getenv('SALES_FORCE_SECRET')
        self.sales_force_access_key = os.getenv('SALES_FORCE_ACCESS_KEY')
        self.sales_force_callback = os.getenv('SALES_FORCE_CALLBACK_URL')

        self.cloud_elements = CloudElements(
            user_secret=self.user_secret,
            org_secret=self.org_secret
        )

    def test_get_sales_force_provision_url(self):
        resp = self.cloud_elements.get_sales_force_provision_url(
            key=self.sales_force_access_key,
            secret=self.sales_force_secret,
            callback_url=self.sales_force_callback
        )

        assert resp.status_code == 200
        assert 'oauthUrl' in resp.json()
        # And its for this reason, PEP8 Rules suck
        assert resp.json() == \
            {
                'oauthUrl':  'https://login.salesforce.com/services/'
                    'oauth2/authorize?response_type=code&'
                    'client_id={key}&client_secret={secret}'
                    '&scope=full%20refresh_token'
                    '&redirect_uri={callback}'
                    '&state=sfdc'
                    .format(
                        key=self.sales_force_access_key,
                        secret=self.sales_force_secret,
                        callback=self.sales_force_callback,
                    ),
                'element':  'sfdc'
            }

    def test_get_instances(self):
        resp = self.cloud_elements.get_instances()
        assert resp.status_code == 200
        assert resp.json() is not None
        assert type(resp.json()) == list

    def test_get_crm_accounts(self):
        resp = self.cloud_elements.get_instances()
        assert resp.status_code == 200
        instances = resp.json()
        instance = instances.pop()
        self.cloud_elements.element_token = instance['token']
        resp = self.cloud_elements.get_crm_accounts(query="name like 'Chris'")
        assert resp is not None
        assert type(resp.json()) == list

    def test_crm_account(self):
        #TODO SalesForce Instance needs storage
        resp = self.cloud_elements.get_instances()
        assert resp.status_code == 200
        instances = resp.json()
        assert len(instances) > 0
        instance = instances[0]
        self.cloud_elements.element_token = instance['token']

        resp = self.cloud_elements.create_crm_accounts(data={
            'Name': 'Chris George'
        })
        assert resp.status_code == 200
        account = resp.json()
        acct_id = account['Id']
        assert acct_id is not None
        assert account['Name'] == 'Chris George'

        resp = self.cloud_elements.update_crm_account_by_id(
            acct_id=acct_id,
            data={'Name': 'Test'}
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.json()['Name'] == 'Test'

        resp = self.cloud_elements. \
            delete_crm_account_by_id(acct_id=account['Id'])

        assert resp.status_code == 200

        #fail getting it
        resp = self.cloud_elements.get_crm_account_by_id(acct_id=acct_id)
        assert resp.status_code == 404

    def test_crm_contacts(self):
        resp = self.cloud_elements.get_instances()
        assert resp.status_code == 200
        instances = resp.json()
        assert len(instances) > 0
        instance = instances[0]
        self.cloud_elements.element_token = instance['token']

        resp = self.cloud_elements.get_crm_contacts(query='name like "chris"')
        resp.status_code == 200
        assert resp.json() is not None
        assert type(resp.json()) == list

    def test_crm_leads(self):
        resp = self.cloud_elements.get_instances()
        assert resp.status_code == 200
        instances = resp.json()
        assert len(instances) > 0
        instance = instances[0]
        self.cloud_elements.element_token = instance['token']
        resp = self.cloud_elements.get_crm_leads(query='firstName is not null')
        resp.status_code == 200
        assert resp.json() is not None
        assert type(resp.json()) == list

    """ We're just going to revisit this later
    def test_provision_sales_force_instance(self):
        import random
        name = 'test_instance_%s' % random.randint(0, 1000)
        resp = self.cloud_elements.provision_sales_force_instance(
            key=self.sales_force_access_key,
            secret=self.sales_force_secret,
            callback_url=self.sales_force_callback,
            name=name,
            code='adfasdfadfsdafsadfsadfsaf'
        )
        assert resp.status_code == 200
        data = resp.json()
        assert 'id' in data
        assert data['name'] == name
        assert data['id'] is not None

        #delete instance
        #resp = self.cloud_elements.delete_instance(instance_id=data['id'])
        #assert resp.status_code == 200
    """
