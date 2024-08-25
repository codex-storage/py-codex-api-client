# coding: utf-8

"""
    Codex API

    List of endpoints and interfaces available to Codex API users

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SalesAvailability(BaseModel):
    """
    SalesAvailability
    """ # noqa: E501
    id: Optional[Annotated[str, Field(min_length=66, strict=True, max_length=66)]] = Field(default=None, description="32bits identifier encoded in hex-decimal string.")
    total_size: Optional[StrictStr] = Field(default=None, description="Total size of availability's storage in bytes as decimal string", alias="totalSize")
    duration: Optional[StrictStr] = Field(default=None, description="The duration of the request in seconds as decimal string")
    min_price: Optional[StrictStr] = Field(default=None, description="Minimum price to be paid (in amount of tokens) as decimal string", alias="minPrice")
    max_collateral: Optional[StrictStr] = Field(default=None, description="Maximum collateral user is willing to pay per filled Slot (in amount of tokens) as decimal string", alias="maxCollateral")
    __properties: ClassVar[List[str]] = ["id", "totalSize", "duration", "minPrice", "maxCollateral"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SalesAvailability from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SalesAvailability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "totalSize": obj.get("totalSize"),
            "duration": obj.get("duration"),
            "minPrice": obj.get("minPrice"),
            "maxCollateral": obj.get("maxCollateral")
        })
        return _obj


