# coding: utf-8

"""
    WASM OJ Wonderland API

    You can interact with WASM OJ Wonderland through this API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: jacob@csie.cool
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import woj
from woj.api.auth_api import AuthApi  # noqa: E501
from woj.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = woj.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_auth_get(self):
        """Test case for api_auth_get

        """
        pass

    def test_api_auth_send_post(self):
        """Test case for api_auth_send_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
