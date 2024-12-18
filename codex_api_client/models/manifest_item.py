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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ManifestItem(BaseModel):
    """
    ManifestItem
    """ # noqa: E501
    tree_cid: Optional[StrictStr] = Field(default=None, description="Content Identifier as specified at https://github.com/multiformats/cid", alias="treeCid")
    dataset_size: Optional[StrictInt] = Field(default=None, description="Length of original content in bytes", alias="datasetSize")
    block_size: Optional[StrictInt] = Field(default=None, description="Size of blocks", alias="blockSize")
    protected: Optional[StrictBool] = Field(default=None, description="Indicates if content is protected by erasure-coding")
    filename: Optional[StrictStr] = Field(default=None, description="The original name of the uploaded content (optional)")
    mimetype: Optional[StrictStr] = Field(default=None, description="The original mimetype of the uploaded content (optional)")
    uploaded_at: Optional[StrictInt] = Field(default=None, description="The UTC upload timestamp in seconds", alias="uploadedAt")
    __properties: ClassVar[List[str]] = ["treeCid", "datasetSize", "blockSize", "protected", "filename", "mimetype", "uploadedAt"]

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
        """Create an instance of ManifestItem from a JSON string"""
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
        # set to None if filename (nullable) is None
        # and model_fields_set contains the field
        if self.filename is None and "filename" in self.model_fields_set:
            _dict['filename'] = None

        # set to None if mimetype (nullable) is None
        # and model_fields_set contains the field
        if self.mimetype is None and "mimetype" in self.model_fields_set:
            _dict['mimetype'] = None

        # set to None if uploaded_at (nullable) is None
        # and model_fields_set contains the field
        if self.uploaded_at is None and "uploaded_at" in self.model_fields_set:
            _dict['uploadedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManifestItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "treeCid": obj.get("treeCid"),
            "datasetSize": obj.get("datasetSize"),
            "blockSize": obj.get("blockSize"),
            "protected": obj.get("protected"),
            "filename": obj.get("filename"),
            "mimetype": obj.get("mimetype"),
            "uploadedAt": obj.get("uploadedAt")
        })
        return _obj

