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
from woj.models.api_problem_id_get200_response_problem_testcase_inner import ApiProblemIdGet200ResponseProblemTestcaseInner  # noqa: E501
from woj.rest import ApiException

class TestApiProblemIdGet200ResponseProblemTestcaseInner(unittest.TestCase):
    """ApiProblemIdGet200ResponseProblemTestcaseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiProblemIdGet200ResponseProblemTestcaseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiProblemIdGet200ResponseProblemTestcaseInner`
        """
        model = woj.models.api_problem_id_get200_response_problem_testcase_inner.ApiProblemIdGet200ResponseProblemTestcaseInner()  # noqa: E501
        if include_optional :
            return ApiProblemIdGet200ResponseProblemTestcaseInner(
                score = 1.337, 
                description = '', 
                sample = True, 
                stdin = '', 
                stdout = '', 
                stdin_file = '', 
                stdout_file = ''
            )
        else :
            return ApiProblemIdGet200ResponseProblemTestcaseInner(
                score = 1.337,
        )
        """

    def testApiProblemIdGet200ResponseProblemTestcaseInner(self):
        """Test ApiProblemIdGet200ResponseProblemTestcaseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()