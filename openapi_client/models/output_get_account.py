# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OutputGetAccount(BaseModel):
    """
    OutputGetAccount
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, description="A URL to the JSON Schema for this object.", alias="$schema")
    balance: StrictStr = Field(description="The current balance of the account in wei", alias="Balance")
    code_hash: StrictStr = Field(description="A 32 byte hash of the code of the account", alias="CodeHash")
    nonce: StrictStr = Field(description="The transaction count of an account", alias="Nonce")
    storage_root: StrictStr = Field(description="The hash of the account's storage data", alias="StorageRoot")
    __properties: ClassVar[List[str]] = ["$schema", "Balance", "CodeHash", "Nonce", "StorageRoot"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OutputGetAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "var_schema",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutputGetAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "Balance": obj.get("Balance"),
            "CodeHash": obj.get("CodeHash"),
            "Nonce": obj.get("Nonce"),
            "StorageRoot": obj.get("StorageRoot")
        })
        return _obj

