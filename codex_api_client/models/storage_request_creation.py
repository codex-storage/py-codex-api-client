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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class StorageRequestCreation(BaseModel):
    """
    StorageRequestCreation
    """ # noqa: E501
    duration: StrictInt = Field(description="The duration of the request in seconds")
    price_per_byte_per_second: StrictStr = Field(description="The amount of tokens paid per byte per second per slot to hosts the client is willing to pay", alias="pricePerBytePerSecond")
    proof_probability: StrictStr = Field(description="How often storage proofs are required as decimal string", alias="proofProbability")
    nodes: Optional[StrictInt] = Field(default=3, description="Minimal number of nodes the content should be stored on")
    tolerance: Optional[StrictInt] = Field(default=1, description="Additional number of nodes on top of the `nodes` property that can be lost before pronouncing the content lost")
    collateral_per_byte: StrictStr = Field(description="Number as decimal string that represents how much collateral per byte is asked from hosts that wants to fill a slots", alias="collateralPerByte")
    expiry: StrictInt = Field(description="Number that represents expiry threshold in seconds from when the Request is submitted. When the threshold is reached and the Request does not find requested amount of nodes to host the data, the Request is voided. The number of seconds can not be higher then the Request's duration itself.")
    __properties: ClassVar[List[str]] = ["duration", "pricePerBytePerSecond", "proofProbability", "nodes", "tolerance", "collateralPerByte", "expiry"]

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
        """Create an instance of StorageRequestCreation from a JSON string"""
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
        """Create an instance of StorageRequestCreation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration": obj.get("duration"),
            "pricePerBytePerSecond": obj.get("pricePerBytePerSecond"),
            "proofProbability": obj.get("proofProbability"),
            "nodes": obj.get("nodes") if obj.get("nodes") is not None else 3,
            "tolerance": obj.get("tolerance") if obj.get("tolerance") is not None else 1,
            "collateralPerByte": obj.get("collateralPerByte"),
            "expiry": obj.get("expiry")
        })
        return _obj


