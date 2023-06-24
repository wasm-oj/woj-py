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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ApiProblemIdGet200ResponseProblemTestcaseInner(BaseModel):
    """
    ApiProblemIdGet200ResponseProblemTestcaseInner
    """
    score: Union[StrictFloat, StrictInt] = Field(...)
    description: Optional[StrictStr] = None
    sample: Optional[StrictBool] = None
    stdin: Optional[StrictStr] = None
    stdout: Optional[StrictStr] = None
    stdin_file: Optional[StrictStr] = None
    stdout_file: Optional[StrictStr] = None
    __properties = ["score", "description", "sample", "stdin", "stdout", "stdin_file", "stdout_file"]

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
    def from_json(cls, json_str: str) -> ApiProblemIdGet200ResponseProblemTestcaseInner:
        """Create an instance of ApiProblemIdGet200ResponseProblemTestcaseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiProblemIdGet200ResponseProblemTestcaseInner:
        """Create an instance of ApiProblemIdGet200ResponseProblemTestcaseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiProblemIdGet200ResponseProblemTestcaseInner.parse_obj(obj)

        _obj = ApiProblemIdGet200ResponseProblemTestcaseInner.parse_obj({
            "score": obj.get("score"),
            "description": obj.get("description"),
            "sample": obj.get("sample"),
            "stdin": obj.get("stdin"),
            "stdout": obj.get("stdout"),
            "stdin_file": obj.get("stdin_file"),
            "stdout_file": obj.get("stdout_file")
        })
        return _obj

