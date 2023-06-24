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
from woj.models.api_sys_get200_response_stat import ApiSysGet200ResponseStat  # noqa: E501
from woj.rest import ApiException

class TestApiSysGet200ResponseStat(unittest.TestCase):
    """ApiSysGet200ResponseStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiSysGet200ResponseStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiSysGet200ResponseStat`
        """
        model = woj.models.api_sys_get200_response_stat.ApiSysGet200ResponseStat()  # noqa: E501
        if include_optional :
            return ApiSysGet200ResponseStat(
                user = 1.337, 
                submission = 1.337, 
                problem = 1.337
            )
        else :
            return ApiSysGet200ResponseStat(
                user = 1.337,
                submission = 1.337,
                problem = 1.337,
        )
        """

    def testApiSysGet200ResponseStat(self):
        """Test ApiSysGet200ResponseStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()