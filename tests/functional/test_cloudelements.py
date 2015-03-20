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
