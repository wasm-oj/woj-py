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
from woj.models.api_problem_id_get200_response_problem_policy_inner import ApiProblemIdGet200ResponseProblemPolicyInner  # noqa: E501
from woj.rest import ApiException

class TestApiProblemIdGet200ResponseProblemPolicyInner(unittest.TestCase):
    """ApiProblemIdGet200ResponseProblemPolicyInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiProblemIdGet200ResponseProblemPolicyInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiProblemIdGet200ResponseProblemPolicyInner`
        """
        model = woj.models.api_problem_id_get200_response_problem_policy_inner.ApiProblemIdGet200ResponseProblemPolicyInner()  # noqa: E501
        if include_optional :
            return ApiProblemIdGet200ResponseProblemPolicyInner(
                budget = 1.337, 
                memory = 1.337, 
                score = 1.337
            )
        else :
            return ApiProblemIdGet200ResponseProblemPolicyInner(
                budget = 1.337,
                memory = 1.337,
                score = 1.337,
        )
        """

    def testApiProblemIdGet200ResponseProblemPolicyInner(self):
        """Test ApiProblemIdGet200ResponseProblemPolicyInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
