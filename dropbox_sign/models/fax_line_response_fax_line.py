# coding: utf-8

"""
    Dropbox Sign API

    Dropbox Sign v3 API

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dropbox_sign.models.account_response import AccountResponse
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class FaxLineResponseFaxLine(BaseModel):
    """
    FaxLineResponseFaxLine
    """  # noqa: E501

    number: Optional[StrictStr] = Field(default=None, description="Number")
    created_at: Optional[StrictInt] = Field(default=None, description="Created at")
    updated_at: Optional[StrictInt] = Field(default=None, description="Updated at")
    accounts: Optional[List[AccountResponse]] = None
    __properties: ClassVar[List[str]] = [
        "number",
        "created_at",
        "updated_at",
        "accounts",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    def to_json_form_params(
        self, excluded_fields: Set[str] = None
    ) -> List[Tuple[str, str]]:
        data: List[Tuple[str, str]] = []

        for key, value in self.to_dict(excluded_fields).items():
            if isinstance(value, (int, str, bool)):
                data.append((key, value))
            else:
                data.append((key, json.dumps(value, ensure_ascii=False)))

        return data

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FaxLineResponseFaxLine from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self, excluded_fields: Set[str] = None) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in accounts (list)
        _items = []
        if self.accounts:
            for _item_accounts in self.accounts:
                if _item_accounts:
                    _items.append(_item_accounts.to_dict())
            _dict["accounts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaxLineResponseFaxLine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "number": obj.get("number"),
                "created_at": obj.get("created_at"),
                "updated_at": obj.get("updated_at"),
                "accounts": (
                    [AccountResponse.from_dict(_item) for _item in obj["accounts"]]
                    if obj.get("accounts") is not None
                    else None
                ),
            }
        )
        return _obj

    @classmethod
    def init(cls, data: Any) -> Self:
        """
        Attempt to instantiate and hydrate a new instance of this class
        """
        if isinstance(data, str):
            data = json.loads(data)

        return cls.from_dict(data)

    @classmethod
    def openapi_types(cls) -> Dict[str, str]:
        return {
            "number": "(str,)",
            "created_at": "(int,)",
            "updated_at": "(int,)",
            "accounts": "(List[AccountResponse],)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "accounts",
        ]
