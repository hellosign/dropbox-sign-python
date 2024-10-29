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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dropbox_sign.models.account_response import AccountResponse
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class TeamResponse(BaseModel):
    """
    Contains information about your team and its members
    """  # noqa: E501

    name: Optional[StrictStr] = Field(default=None, description="The name of your Team")
    accounts: Optional[List[AccountResponse]] = None
    invited_accounts: Optional[List[AccountResponse]] = Field(
        default=None,
        description="A list of all Accounts that have an outstanding invitation to join your Team. Note that this response is a subset of the response parameters found in `GET /account`.",
    )
    invited_emails: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of email addresses that have an outstanding invitation to join your Team and do not yet have a Dropbox Sign account.",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "accounts",
        "invited_accounts",
        "invited_emails",
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
        """Create an instance of TeamResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in invited_accounts (list)
        _items = []
        if self.invited_accounts:
            for _item_invited_accounts in self.invited_accounts:
                if _item_invited_accounts:
                    _items.append(_item_invited_accounts.to_dict())
            _dict["invited_accounts"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TeamResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "accounts": (
                    [AccountResponse.from_dict(_item) for _item in obj["accounts"]]
                    if obj.get("accounts") is not None
                    else None
                ),
                "invited_accounts": (
                    [
                        AccountResponse.from_dict(_item)
                        for _item in obj["invited_accounts"]
                    ]
                    if obj.get("invited_accounts") is not None
                    else None
                ),
                "invited_emails": obj.get("invited_emails"),
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
            "name": "(str,)",
            "accounts": "(List[AccountResponse],)",
            "invited_accounts": "(List[AccountResponse],)",
            "invited_emails": "(List[str],)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "accounts",
            "invited_accounts",
            "invited_emails",
        ]