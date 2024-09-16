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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from dropbox_sign.models.sub_attachment import SubAttachment
from dropbox_sign.models.sub_field_options import SubFieldOptions
from dropbox_sign.models.sub_form_field_group import SubFormFieldGroup
from dropbox_sign.models.sub_form_field_rule import SubFormFieldRule
from dropbox_sign.models.sub_form_fields_per_document_base import (
    SubFormFieldsPerDocumentBase,
)
from dropbox_sign.models.sub_merge_field import SubMergeField
from dropbox_sign.models.sub_template_role import SubTemplateRole
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class TemplateCreateRequest(BaseModel):
    """
    TemplateCreateRequest
    """  # noqa: E501

    form_fields_per_document: List[SubFormFieldsPerDocumentBase] = Field(
        description="The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)  **NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.  * Text Field use `SubFormFieldsPerDocumentText` * Dropdown Field use `SubFormFieldsPerDocumentDropdown` * Hyperlink Field use `SubFormFieldsPerDocumentHyperlink` * Checkbox Field use `SubFormFieldsPerDocumentCheckbox` * Radio Field use `SubFormFieldsPerDocumentRadio` * Signature Field use `SubFormFieldsPerDocumentSignature` * Date Signed Field use `SubFormFieldsPerDocumentDateSigned` * Initials Field use `SubFormFieldsPerDocumentInitials` * Text Merge Field use `SubFormFieldsPerDocumentTextMerge` * Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`"
    )
    signer_roles: List[SubTemplateRole] = Field(
        description="An array of the designated signer roles that must be specified when sending a SignatureRequest using this Template."
    )
    files: Optional[List[Union[StrictBytes, StrictStr, io.IOBase]]] = Field(
        default=None,
        description="Use `files[]` to indicate the uploaded file(s) to send for signature.  This endpoint requires either **files** or **file_urls[]**, but not both.",
    )
    file_urls: Optional[List[StrictStr]] = Field(
        default=None,
        description="Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.  This endpoint requires either **files** or **file_urls[]**, but not both.",
    )
    allow_reassign: Optional[StrictBool] = Field(
        default=False,
        description="Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.  **NOTE:** Only available for Premium plan and higher.",
    )
    attachments: Optional[List[SubAttachment]] = Field(
        default=None, description="A list describing the attachments"
    )
    cc_roles: Optional[List[StrictStr]] = Field(
        default=None,
        description="The CC roles that must be assigned when using the template to send a signature request",
    )
    client_id: Optional[StrictStr] = Field(
        default=None,
        description="Client id of the app you're using to create this draft. Used to apply the branding and callback url defined for the app.",
    )
    field_options: Optional[SubFieldOptions] = None
    form_field_groups: Optional[List[SubFormFieldGroup]] = Field(
        default=None,
        description="Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.",
    )
    form_field_rules: Optional[List[SubFormFieldRule]] = Field(
        default=None,
        description="Conditional Logic rules for fields defined in `form_fields_per_document`.",
    )
    merge_fields: Optional[List[SubMergeField]] = Field(
        default=None,
        description="Add merge fields to the template. Merge fields are placed by the user creating the template and used to pre-fill data by passing values into signature requests with the `custom_fields` parameter. If the signature request using that template *does not* pass a value into a merge field, then an empty field remains in the document.",
    )
    message: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = Field(
        default=None, description="The default template email message."
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.  Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.",
    )
    subject: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(
        default=None, description="The template title (alias)."
    )
    test_mode: Optional[StrictBool] = Field(
        default=False,
        description="Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.",
    )
    title: Optional[StrictStr] = Field(
        default=None,
        description="The title you want to assign to the SignatureRequest.",
    )
    use_preexisting_fields: Optional[StrictBool] = Field(
        default=False,
        description="Enable the detection of predefined PDF fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`).",
    )
    __properties: ClassVar[List[str]] = [
        "form_fields_per_document",
        "signer_roles",
        "files",
        "file_urls",
        "allow_reassign",
        "attachments",
        "cc_roles",
        "client_id",
        "field_options",
        "form_field_groups",
        "form_field_rules",
        "merge_fields",
        "message",
        "metadata",
        "subject",
        "test_mode",
        "title",
        "use_preexisting_fields",
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
        """Create an instance of TemplateCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in form_fields_per_document (list)
        _items = []
        if self.form_fields_per_document:
            for _item_form_fields_per_document in self.form_fields_per_document:
                if _item_form_fields_per_document:
                    _items.append(_item_form_fields_per_document.to_dict())
            _dict["form_fields_per_document"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in signer_roles (list)
        _items = []
        if self.signer_roles:
            for _item_signer_roles in self.signer_roles:
                if _item_signer_roles:
                    _items.append(_item_signer_roles.to_dict())
            _dict["signer_roles"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict["attachments"] = _items
        # override the default output from pydantic by calling `to_dict()` of field_options
        if self.field_options:
            _dict["field_options"] = self.field_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in form_field_groups (list)
        _items = []
        if self.form_field_groups:
            for _item_form_field_groups in self.form_field_groups:
                if _item_form_field_groups:
                    _items.append(_item_form_field_groups.to_dict())
            _dict["form_field_groups"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_field_rules (list)
        _items = []
        if self.form_field_rules:
            for _item_form_field_rules in self.form_field_rules:
                if _item_form_field_rules:
                    _items.append(_item_form_field_rules.to_dict())
            _dict["form_field_rules"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in merge_fields (list)
        _items = []
        if self.merge_fields:
            for _item_merge_fields in self.merge_fields:
                if _item_merge_fields:
                    _items.append(_item_merge_fields.to_dict())
            _dict["merge_fields"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemplateCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "form_fields_per_document": (
                    [
                        SubFormFieldsPerDocumentBase.from_dict(_item)
                        for _item in obj["form_fields_per_document"]
                    ]
                    if obj.get("form_fields_per_document") is not None
                    else None
                ),
                "signer_roles": (
                    [SubTemplateRole.from_dict(_item) for _item in obj["signer_roles"]]
                    if obj.get("signer_roles") is not None
                    else None
                ),
                "files": obj.get("files"),
                "file_urls": obj.get("file_urls"),
                "allow_reassign": (
                    obj.get("allow_reassign")
                    if obj.get("allow_reassign") is not None
                    else False
                ),
                "attachments": (
                    [SubAttachment.from_dict(_item) for _item in obj["attachments"]]
                    if obj.get("attachments") is not None
                    else None
                ),
                "cc_roles": obj.get("cc_roles"),
                "client_id": obj.get("client_id"),
                "field_options": (
                    SubFieldOptions.from_dict(obj["field_options"])
                    if obj.get("field_options") is not None
                    else None
                ),
                "form_field_groups": (
                    [
                        SubFormFieldGroup.from_dict(_item)
                        for _item in obj["form_field_groups"]
                    ]
                    if obj.get("form_field_groups") is not None
                    else None
                ),
                "form_field_rules": (
                    [
                        SubFormFieldRule.from_dict(_item)
                        for _item in obj["form_field_rules"]
                    ]
                    if obj.get("form_field_rules") is not None
                    else None
                ),
                "merge_fields": (
                    [SubMergeField.from_dict(_item) for _item in obj["merge_fields"]]
                    if obj.get("merge_fields") is not None
                    else None
                ),
                "message": obj.get("message"),
                "metadata": obj.get("metadata"),
                "subject": obj.get("subject"),
                "test_mode": (
                    obj.get("test_mode") if obj.get("test_mode") is not None else False
                ),
                "title": obj.get("title"),
                "use_preexisting_fields": (
                    obj.get("use_preexisting_fields")
                    if obj.get("use_preexisting_fields") is not None
                    else False
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
            "form_fields_per_document": "(List[SubFormFieldsPerDocumentBase],)",
            "signer_roles": "(List[SubTemplateRole],)",
            "files": "(List[io.IOBase],)",
            "file_urls": "(List[str],)",
            "allow_reassign": "(bool,)",
            "attachments": "(List[SubAttachment],)",
            "cc_roles": "(List[str],)",
            "client_id": "(str,)",
            "field_options": "(SubFieldOptions,)",
            "form_field_groups": "(List[SubFormFieldGroup],)",
            "form_field_rules": "(List[SubFormFieldRule],)",
            "merge_fields": "(List[SubMergeField],)",
            "message": "(str,)",
            "metadata": "(Dict[str, object],)",
            "subject": "(str,)",
            "test_mode": "(bool,)",
            "title": "(str,)",
            "use_preexisting_fields": "(bool,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "form_fields_per_document",
            "signer_roles",
            "files",
            "file_urls",
            "attachments",
            "cc_roles",
            "form_field_groups",
            "form_field_rules",
            "merge_fields",
        ]
