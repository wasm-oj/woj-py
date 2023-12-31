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
import datetime

import woj
from woj.models.api_auth_send_post200_response import ApiAuthSendPost200Response  # noqa: E501
from woj.rest import ApiException

class TestApiAuthSendPost200Response(unittest.TestCase):
    """ApiAuthSendPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiAuthSendPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAuthSendPost200Response`
        """
        model = woj.models.api_auth_send_post200_response.ApiAuthSendPost200Response()  # noqa: E501
        if include_optional :
            return ApiAuthSendPost200Response(
                ok = True, 
                send = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ApiAuthSendPost200Response(
                ok = True,
                send = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testApiAuthSendPost200Response(self):
        """Test ApiAuthSendPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
