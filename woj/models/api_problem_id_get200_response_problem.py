# coding: utf-8

"""
    WASM OJ Wonderland API

    You can interact with WASM OJ Wonderland through this API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: jacob@csie.cool
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from woj.models.api_problem_id_get200_response_problem_policy_inner import ApiProblemIdGet200ResponseProblemPolicyInner
from woj.models.api_problem_id_get200_response_problem_testcase_inner import ApiProblemIdGet200ResponseProblemTestcaseInner

class ApiProblemIdGet200ResponseProblem(BaseModel):
    """
    ApiProblemIdGet200ResponseProblem
    """
    name: StrictStr = Field(...)
    tags: Optional[conlist(StrictStr)] = None
    description: StrictStr = Field(...)
    policy: conlist(ApiProblemIdGet200ResponseProblemPolicyInner) = Field(...)
    testcase: conlist(ApiProblemIdGet200ResponseProblemTestcaseInner) = Field(...)
    input: Optional[StrictStr] = None
    output: Optional[StrictStr] = None
    hint: Optional[StrictStr] = None
    __properties = ["name", "tags", "description", "policy", "testcase", "input", "output", "hint"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiProblemIdGet200ResponseProblem:
        """Create an instance of ApiProblemIdGet200ResponseProblem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in policy (list)
        _items = []
        if self.policy:
            for _item in self.policy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policy'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in testcase (list)
        _items = []
        if self.testcase:
            for _item in self.testcase:
                if _item:
                    _items.append(_item.to_dict())
            _dict['testcase'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiProblemIdGet200ResponseProblem:
        """Create an instance of ApiProblemIdGet200ResponseProblem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiProblemIdGet200ResponseProblem.parse_obj(obj)

        _obj = ApiProblemIdGet200ResponseProblem.parse_obj({
            "name": obj.get("name"),
            "tags": obj.get("tags"),
            "description": obj.get("description"),
            "policy": [ApiProblemIdGet200ResponseProblemPolicyInner.from_dict(_item) for _item in obj.get("policy")] if obj.get("policy") is not None else None,
            "testcase": [ApiProblemIdGet200ResponseProblemTestcaseInner.from_dict(_item) for _item in obj.get("testcase")] if obj.get("testcase") is not None else None,
            "input": obj.get("input"),
            "output": obj.get("output"),
            "hint": obj.get("hint")
        })
        return _obj

