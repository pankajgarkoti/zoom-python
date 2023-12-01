# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.pac_api import PACApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPACApi(unittest.TestCase):
    """PACApi unit test stubs"""

    def setUp(self):
        self.api = PACApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_pacs(self):
        """Test case for user_pacs

        List a user's PAC accounts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
