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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class ApiSysGet200ResponseStat(BaseModel):
    """
    ApiSysGet200ResponseStat
    """
    user: Union[StrictFloat, StrictInt] = Field(..., description="Number of users")
    submission: Union[StrictFloat, StrictInt] = Field(..., description="Number of submissions")
    problem: Union[StrictFloat, StrictInt] = Field(..., description="Number of problems")
    __properties = ["user", "submission", "problem"]

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
    def from_json(cls, json_str: str) -> ApiSysGet200ResponseStat:
        """Create an instance of ApiSysGet200ResponseStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiSysGet200ResponseStat:
        """Create an instance of ApiSysGet200ResponseStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiSysGet200ResponseStat.parse_obj(obj)

        _obj = ApiSysGet200ResponseStat.parse_obj({
            "user": obj.get("user"),
            "submission": obj.get("submission"),
            "problem": obj.get("problem")
        })
        return _obj
