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

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class SubWhiteLabelingOptions(BaseModel):
    """
    An array of elements and values serialized to a string, to be used to customize the app's signer page. (Only applies to some API plans)  Take a look at our [white labeling guide](https://developers.hellosign.com/api/reference/premium-branding/) to learn more.
    """  # noqa: E501

    header_background_color: Optional[StrictStr] = "#1a1a1a"
    legal_version: Optional[StrictStr] = "terms1"
    link_color: Optional[StrictStr] = "#0061FE"
    page_background_color: Optional[StrictStr] = "#f7f8f9"
    primary_button_color: Optional[StrictStr] = "#0061FE"
    primary_button_color_hover: Optional[StrictStr] = "#0061FE"
    primary_button_text_color: Optional[StrictStr] = "#ffffff"
    primary_button_text_color_hover: Optional[StrictStr] = "#ffffff"
    secondary_button_color: Optional[StrictStr] = "#ffffff"
    secondary_button_color_hover: Optional[StrictStr] = "#ffffff"
    secondary_button_text_color: Optional[StrictStr] = "#0061FE"
    secondary_button_text_color_hover: Optional[StrictStr] = "#0061FE"
    text_color1: Optional[StrictStr] = "#808080"
    text_color2: Optional[StrictStr] = "#ffffff"
    reset_to_default: Optional[StrictBool] = Field(
        default=None,
        description="Resets white labeling options to defaults. Only useful when updating an API App.",
    )
    __properties: ClassVar[List[str]] = [
        "header_background_color",
        "legal_version",
        "link_color",
        "page_background_color",
        "primary_button_color",
        "primary_button_color_hover",
        "primary_button_text_color",
        "primary_button_text_color_hover",
        "secondary_button_color",
        "secondary_button_color_hover",
        "secondary_button_text_color",
        "secondary_button_text_color_hover",
        "text_color1",
        "text_color2",
        "reset_to_default",
    ]

    @field_validator("legal_version")
    def legal_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(["terms1", "terms2"]):
            raise ValueError("must be one of enum values ('terms1', 'terms2')")
        return value

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
        """Create an instance of SubWhiteLabelingOptions from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubWhiteLabelingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "header_background_color": (
                    obj.get("header_background_color")
                    if obj.get("header_background_color") is not None
                    else "#1a1a1a"
                ),
                "legal_version": (
                    obj.get("legal_version")
                    if obj.get("legal_version") is not None
                    else "terms1"
                ),
                "link_color": (
                    obj.get("link_color")
                    if obj.get("link_color") is not None
                    else "#0061FE"
                ),
                "page_background_color": (
                    obj.get("page_background_color")
                    if obj.get("page_background_color") is not None
                    else "#f7f8f9"
                ),
                "primary_button_color": (
                    obj.get("primary_button_color")
                    if obj.get("primary_button_color") is not None
                    else "#0061FE"
                ),
                "primary_button_color_hover": (
                    obj.get("primary_button_color_hover")
                    if obj.get("primary_button_color_hover") is not None
                    else "#0061FE"
                ),
                "primary_button_text_color": (
                    obj.get("primary_button_text_color")
                    if obj.get("primary_button_text_color") is not None
                    else "#ffffff"
                ),
                "primary_button_text_color_hover": (
                    obj.get("primary_button_text_color_hover")
                    if obj.get("primary_button_text_color_hover") is not None
                    else "#ffffff"
                ),
                "secondary_button_color": (
                    obj.get("secondary_button_color")
                    if obj.get("secondary_button_color") is not None
                    else "#ffffff"
                ),
                "secondary_button_color_hover": (
                    obj.get("secondary_button_color_hover")
                    if obj.get("secondary_button_color_hover") is not None
                    else "#ffffff"
                ),
                "secondary_button_text_color": (
                    obj.get("secondary_button_text_color")
                    if obj.get("secondary_button_text_color") is not None
                    else "#0061FE"
                ),
                "secondary_button_text_color_hover": (
                    obj.get("secondary_button_text_color_hover")
                    if obj.get("secondary_button_text_color_hover") is not None
                    else "#0061FE"
                ),
                "text_color1": (
                    obj.get("text_color1")
                    if obj.get("text_color1") is not None
                    else "#808080"
                ),
                "text_color2": (
                    obj.get("text_color2")
                    if obj.get("text_color2") is not None
                    else "#ffffff"
                ),
                "reset_to_default": obj.get("reset_to_default"),
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
            "header_background_color": "(str,)",
            "legal_version": "(str,)",
            "link_color": "(str,)",
            "page_background_color": "(str,)",
            "primary_button_color": "(str,)",
            "primary_button_color_hover": "(str,)",
            "primary_button_text_color": "(str,)",
            "primary_button_text_color_hover": "(str,)",
            "secondary_button_color": "(str,)",
            "secondary_button_color_hover": "(str,)",
            "secondary_button_text_color": "(str,)",
            "secondary_button_text_color_hover": "(str,)",
            "text_color1": "(str,)",
            "text_color2": "(str,)",
            "reset_to_default": "(bool,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in []
