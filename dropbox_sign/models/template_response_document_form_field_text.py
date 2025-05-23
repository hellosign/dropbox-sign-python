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
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional
from dropbox_sign.models.template_response_document_form_field_base import (
    TemplateResponseDocumentFormFieldBase,
)
from dropbox_sign.models.template_response_field_avg_text_length import (
    TemplateResponseFieldAvgTextLength,
)
from typing import Optional, Set
from typing_extensions import Self
from typing import Tuple, Union
import io
from pydantic import StrictBool


class TemplateResponseDocumentFormFieldText(TemplateResponseDocumentFormFieldBase):
    """
    This class extends `TemplateResponseDocumentFormFieldBase`
    """  # noqa: E501

    type: StrictStr = Field(
        description="The type of this form field. See [field types](/api/reference/constants/#field-types).  * Text Field uses `TemplateResponseDocumentFormFieldText` * Dropdown Field uses `TemplateResponseDocumentFormFieldDropdown` * Hyperlink Field uses `TemplateResponseDocumentFormFieldHyperlink` * Checkbox Field uses `TemplateResponseDocumentFormFieldCheckbox` * Radio Field uses `TemplateResponseDocumentFormFieldRadio` * Signature Field uses `TemplateResponseDocumentFormFieldSignature` * Date Signed Field uses `TemplateResponseDocumentFormFieldDateSigned` * Initials Field uses `TemplateResponseDocumentFormFieldInitials`"
    )
    avg_text_length: Optional[TemplateResponseFieldAvgTextLength] = None
    is_multiline: Optional[StrictBool] = Field(
        default=None,
        description="Whether this form field is multiline text.",
        alias="isMultiline",
    )
    original_font_size: Optional[StrictInt] = Field(
        default=None,
        description="Original font size used in this form field's text.",
        alias="originalFontSize",
    )
    font_family: Optional[StrictStr] = Field(
        default=None,
        description="Font family used in this form field's text.",
        alias="fontFamily",
    )
    validation_type: Optional[StrictStr] = Field(
        default=None,
        description="Each text field may contain a `validation_type` parameter. Check out the list of [validation types](https://faq.hellosign.com/hc/en-us/articles/217115577) to learn more about the possible values.",
    )
    group: Optional[StrictStr] = Field(
        default=None,
        description="The name of the group this field is in. If this field is not a group, this defaults to `null` except for Radio fields.",
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "api_id",
        "name",
        "signer",
        "x",
        "y",
        "width",
        "height",
        "required",
        "avg_text_length",
        "isMultiline",
        "originalFontSize",
        "fontFamily",
        "validation_type",
        "group",
    ]

    @field_validator("validation_type")
    def validation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "numbers_only",
                "letters_only",
                "phone_number",
                "bank_routing_number",
                "bank_account_number",
                "email_address",
                "zip_code",
                "social_security_number",
                "employer_identification_number",
                "custom_regex",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('numbers_only', 'letters_only', 'phone_number', 'bank_routing_number', 'bank_account_number', 'email_address', 'zip_code', 'social_security_number', 'employer_identification_number', 'custom_regex')"
            )
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
        """Create an instance of TemplateResponseDocumentFormFieldText from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of avg_text_length
        if self.avg_text_length:
            _dict["avg_text_length"] = self.avg_text_length.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemplateResponseDocumentFormFieldText from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type") if obj.get("type") is not None else "text",
                "api_id": obj.get("api_id"),
                "name": obj.get("name"),
                "signer": obj.get("signer"),
                "x": obj.get("x"),
                "y": obj.get("y"),
                "width": obj.get("width"),
                "height": obj.get("height"),
                "required": obj.get("required"),
                "avg_text_length": (
                    TemplateResponseFieldAvgTextLength.from_dict(obj["avg_text_length"])
                    if obj.get("avg_text_length") is not None
                    else None
                ),
                "isMultiline": obj.get("isMultiline"),
                "originalFontSize": obj.get("originalFontSize"),
                "fontFamily": obj.get("fontFamily"),
                "validation_type": obj.get("validation_type"),
                "group": obj.get("group"),
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
            "type": "(str,)",
            "avg_text_length": "(TemplateResponseFieldAvgTextLength,)",
            "is_multiline": "(bool,)",
            "original_font_size": "(int,)",
            "font_family": "(str,)",
            "validation_type": "(str,)",
            "group": "(str,)",
            "api_id": "(str,)",
            "name": "(str,)",
            "signer": "(int, str,)",
            "x": "(int,)",
            "y": "(int,)",
            "width": "(int,)",
            "height": "(int,)",
            "required": "(bool,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in []
