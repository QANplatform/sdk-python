# coding: utf-8

"""
    QAN AutoApi

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from qan.models.response_log import ResponseLog
from typing import Optional, Set
from typing_extensions import Self

class ResponseTransactionReceipt(BaseModel):
    """
    ResponseTransactionReceipt
    """ # noqa: E501
    block_hash: Optional[StrictStr] = Field(default=None, description="The hash of the block. null when pending", alias="BlockHash")
    block_number: Optional[StrictStr] = Field(default=None, alias="BlockNumber")
    contract_address: Optional[StrictStr] = Field(default=None, description="The contract address created if the transaction was a contract creation, otherwise null", alias="ContractAddress")
    cumulative_gas_used: Optional[StrictStr] = Field(default=None, description="The total amount of gas used when this transaction was executed in the block", alias="CumulativeGasUsed")
    effective_gas_price: Optional[StrictStr] = Field(default=None, description="The actual value per gas deducted from the sender account", alias="EffectiveGasPrice")
    var_from: Optional[StrictStr] = Field(default=None, description="The address of the sender", alias="From")
    gas_used: Optional[StrictStr] = Field(default=None, description="The amount of gas used by this specific transaction alone", alias="GasUsed")
    logs: Optional[List[ResponseLog]] = Field(default=None, description="An array of log objects that generated this transaction", alias="Logs")
    logs_bloom: Optional[StrictStr] = Field(default=None, description="The bloom filter for light clients to quickly retrieve related logs", alias="LogsBloom")
    status: Optional[StrictStr] = Field(default=None, description="It is either 1 (success) or 0 (failure) encoded as a decimal", alias="Status")
    to: Optional[StrictStr] = Field(default=None, description="The address of the receiver. null when it's a contract creation transaction", alias="To")
    transaction_hash: Optional[StrictStr] = Field(default=None, description="The hash of the transaction", alias="TransactionHash")
    transaction_index: Optional[StrictStr] = Field(default=None, description="An index of the transaction in the block", alias="TransactionIndex")
    type: Optional[StrictStr] = Field(default=None, description="The value type", alias="Type")
    __properties: ClassVar[List[str]] = ["BlockHash", "BlockNumber", "ContractAddress", "CumulativeGasUsed", "EffectiveGasPrice", "From", "GasUsed", "Logs", "LogsBloom", "Status", "To", "TransactionHash", "TransactionIndex", "Type"]

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
        """Create an instance of ResponseTransactionReceipt from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in logs (list)
        _items = []
        if self.logs:
            for _item_logs in self.logs:
                if _item_logs:
                    _items.append(_item_logs.to_dict())
            _dict['Logs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseTransactionReceipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "BlockHash": obj.get("BlockHash"),
            "BlockNumber": obj.get("BlockNumber"),
            "ContractAddress": obj.get("ContractAddress"),
            "CumulativeGasUsed": obj.get("CumulativeGasUsed"),
            "EffectiveGasPrice": obj.get("EffectiveGasPrice"),
            "From": obj.get("From"),
            "GasUsed": obj.get("GasUsed"),
            "Logs": [ResponseLog.from_dict(_item) for _item in obj["Logs"]] if obj.get("Logs") is not None else None,
            "LogsBloom": obj.get("LogsBloom"),
            "Status": obj.get("Status"),
            "To": obj.get("To"),
            "TransactionHash": obj.get("TransactionHash"),
            "TransactionIndex": obj.get("TransactionIndex"),
            "Type": obj.get("Type")
        })
        return _obj


