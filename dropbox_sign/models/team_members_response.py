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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from dropbox_sign.models.list_info_response import ListInfoResponse
from dropbox_sign.models.team_member_response import TeamMemberResponse
from dropbox_sign.models.warning_response import WarningResponse
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class TeamMembersResponse(BaseModel):
    """
    TeamMembersResponse
    """  # noqa: E501

    team_members: List[TeamMemberResponse] = Field(
        description="Contains a list of team members and their roles for a specific team."
    )
    list_info: ListInfoResponse
    warnings: Optional[List[WarningResponse]] = None
    __properties: ClassVar[List[str]] = ["team_members", "list_info", "warnings"]

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
        """Create an instance of TeamMembersResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in team_members (list)
        _items = []
        if self.team_members:
            for _item_team_members in self.team_members:
                if _item_team_members:
                    _items.append(_item_team_members.to_dict())
            _dict["team_members"] = _items
        # override the default output from pydantic by calling `to_dict()` of list_info
        if self.list_info:
            _dict["list_info"] = self.list_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict["warnings"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TeamMembersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "team_members": (
                    [
                        TeamMemberResponse.from_dict(_item)
                        for _item in obj["team_members"]
                    ]
                    if obj.get("team_members") is not None
                    else None
                ),
                "list_info": (
                    ListInfoResponse.from_dict(obj["list_info"])
                    if obj.get("list_info") is not None
                    else None
                ),
                "warnings": (
                    [WarningResponse.from_dict(_item) for _item in obj["warnings"]]
                    if obj.get("warnings") is not None
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
            "team_members": "(List[TeamMemberResponse],)",
            "list_info": "(ListInfoResponse,)",
            "warnings": "(List[WarningResponse],)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "team_members",
            "warnings",
        ]
