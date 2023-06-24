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



from pydantic import BaseModel, Field, StrictStr, constr, validator

class SubmitRequest(BaseModel):
    """
    SubmitRequest
    """
    problem: constr(strict=True, max_length=128, min_length=1) = Field(..., description="Problem ID")
    code: constr(strict=True, max_length=16384, min_length=1) = Field(..., description="Source code")
    lang: StrictStr = Field(..., description="Programming language of the source code")
    __properties = ["problem", "code", "lang"]

    @validator('lang')
    def lang_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('rs', 'c', 'cpp'):
            raise ValueError("must be one of enum values ('rs', 'c', 'cpp')")
        return value

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
    def from_json(cls, json_str: str) -> SubmitRequest:
        """Create an instance of SubmitRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubmitRequest:
        """Create an instance of SubmitRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubmitRequest.parse_obj(obj)

        _obj = SubmitRequest.parse_obj({
            "problem": obj.get("problem"),
            "code": obj.get("code"),
            "lang": obj.get("lang")
        })
        return _obj
