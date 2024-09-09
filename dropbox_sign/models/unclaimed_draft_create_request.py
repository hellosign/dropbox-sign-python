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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from dropbox_sign.models.sub_attachment import SubAttachment
from dropbox_sign.models.sub_custom_field import SubCustomField
from dropbox_sign.models.sub_field_options import SubFieldOptions
from dropbox_sign.models.sub_form_field_group import SubFormFieldGroup
from dropbox_sign.models.sub_form_field_rule import SubFormFieldRule
from dropbox_sign.models.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase
from dropbox_sign.models.sub_signing_options import SubSigningOptions
from dropbox_sign.models.sub_unclaimed_draft_signer import SubUnclaimedDraftSigner
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class UnclaimedDraftCreateRequest(BaseModel):
    """
    
    """ # noqa: E501
    type: StrictStr = Field(description="The type of unclaimed draft to create. Use `send_document` to create a claimable file, and `request_signature` for a claimable signature request. If the type is `request_signature` then signers name and email_address are not optional.")
    files: Optional[List[Union[StrictBytes, StrictStr, io.IOBase]]] = Field(default=None, description="Use `files[]` to indicate the uploaded file(s) to send for signature.  This endpoint requires either **files** or **file_urls[]**, but not both.")
    file_urls: Optional[List[StrictStr]] = Field(default=None, description="Use `file_urls[]` to have Dropbox Sign download the file(s) to send for signature.  This endpoint requires either **files** or **file_urls[]**, but not both.")
    allow_decline: Optional[StrictBool] = Field(default=False, description="Allows signers to decline to sign a document if `true`. Defaults to `false`.")
    attachments: Optional[List[SubAttachment]] = Field(default=None, description="A list describing the attachments")
    cc_email_addresses: Optional[List[StrictStr]] = Field(default=None, description="The email addresses that should be CCed.")
    client_id: Optional[StrictStr] = Field(default=None, description="Client id of the app used to create the draft. Used to apply the branding and callback url defined for the app.")
    custom_fields: Optional[List[SubCustomField]] = Field(default=None, description="When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.  Pre-filled data can be used with \"send-once\" signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.  For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.")
    field_options: Optional[SubFieldOptions] = None
    form_field_groups: Optional[List[SubFormFieldGroup]] = Field(default=None, description="Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.")
    form_field_rules: Optional[List[SubFormFieldRule]] = Field(default=None, description="Conditional Logic rules for fields defined in `form_fields_per_document`.")
    form_fields_per_document: Optional[List[SubFormFieldsPerDocumentBase]] = Field(default=None, description="The fields that should appear on the document, expressed as an array of objects. (For more details you can read about it here: [Using Form Fields per Document](/docs/openapi/form-fields-per-document).)  **NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](/api/reference/constants/#form-fields-per-document) for these field types.  * Text Field use `SubFormFieldsPerDocumentText` * Dropdown Field use `SubFormFieldsPerDocumentDropdown` * Hyperlink Field use `SubFormFieldsPerDocumentHyperlink` * Checkbox Field use `SubFormFieldsPerDocumentCheckbox` * Radio Field use `SubFormFieldsPerDocumentRadio` * Signature Field use `SubFormFieldsPerDocumentSignature` * Date Signed Field use `SubFormFieldsPerDocumentDateSigned` * Initials Field use `SubFormFieldsPerDocumentInitials` * Text Merge Field use `SubFormFieldsPerDocumentTextMerge` * Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`")
    hide_text_tags: Optional[StrictBool] = Field(default=False, description="Send with a value of `true` if you wish to enable automatic Text Tag removal. Defaults to `false`. When using Text Tags it is preferred that you set this to `false` and hide your tags with white text or something similar because the automatic removal system can cause unwanted clipping. See the [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) walkthrough for more details.")
    message: Optional[Annotated[str, Field(strict=True, max_length=5000)]] = Field(default=None, description="The custom message in the email that will be sent to the signers.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.  Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.")
    show_progress_stepper: Optional[StrictBool] = Field(default=True, description="When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.")
    signers: Optional[List[SubUnclaimedDraftSigner]] = Field(default=None, description="Add Signers to your Unclaimed Draft Signature Request.")
    signing_options: Optional[SubSigningOptions] = None
    signing_redirect_url: Optional[StrictStr] = Field(default=None, description="The URL you want signers redirected to after they successfully sign.")
    subject: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The subject in the email that will be sent to the signers.")
    test_mode: Optional[StrictBool] = Field(default=False, description="Whether this is a test, the signature request created from this draft will not be legally binding if set to `true`. Defaults to `false`.")
    use_preexisting_fields: Optional[StrictBool] = Field(default=False, description="Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.")
    use_text_tags: Optional[StrictBool] = Field(default=False, description="Set `use_text_tags` to `true` to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document (defaults to disabled, or `false`). Alternatively, if your PDF contains pre-defined fields, enable the detection of these fields by setting the `use_preexisting_fields` to `true` (defaults to disabled, or `false`). Currently we only support use of either `use_text_tags` or `use_preexisting_fields` parameter, not both.")
    expires_at: Optional[StrictInt] = Field(default=None, description="When the signature request will expire. Unsigned signatures will be moved to the expired status, and no longer signable. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.  **NOTE:** This does not correspond to the **expires_at** returned in the response.")
    __properties: ClassVar[List[str]] = ["type", "files", "file_urls", "allow_decline", "attachments", "cc_email_addresses", "client_id", "custom_fields", "field_options", "form_field_groups", "form_field_rules", "form_fields_per_document", "hide_text_tags", "message", "metadata", "show_progress_stepper", "signers", "signing_options", "signing_redirect_url", "subject", "test_mode", "use_preexisting_fields", "use_text_tags", "expires_at"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['send_document', 'request_signature']):
            raise ValueError("must be one of enum values ('send_document', 'request_signature')")
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

    def to_json_form_params(self, excluded_fields: Set[str] = None) -> List[Tuple[str, str]]:
        data: List[Tuple[str, str]] = []

        for key, value in self.to_dict(excluded_fields).items():
            if isinstance(value, (int, str, bool)):
                data.append((key, value))
            else:
                data.append((key, json.dumps(value, ensure_ascii=False)))

        return data

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UnclaimedDraftCreateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict['custom_fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of field_options
        if self.field_options:
            _dict['field_options'] = self.field_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in form_field_groups (list)
        _items = []
        if self.form_field_groups:
            for _item_form_field_groups in self.form_field_groups:
                if _item_form_field_groups:
                    _items.append(_item_form_field_groups.to_dict())
            _dict['form_field_groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_field_rules (list)
        _items = []
        if self.form_field_rules:
            for _item_form_field_rules in self.form_field_rules:
                if _item_form_field_rules:
                    _items.append(_item_form_field_rules.to_dict())
            _dict['form_field_rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_fields_per_document (list)
        _items = []
        if self.form_fields_per_document:
            for _item_form_fields_per_document in self.form_fields_per_document:
                if _item_form_fields_per_document:
                    _items.append(_item_form_fields_per_document.to_dict())
            _dict['form_fields_per_document'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in signers (list)
        _items = []
        if self.signers:
            for _item_signers in self.signers:
                if _item_signers:
                    _items.append(_item_signers.to_dict())
            _dict['signers'] = _items
        # override the default output from pydantic by calling `to_dict()` of signing_options
        if self.signing_options:
            _dict['signing_options'] = self.signing_options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnclaimedDraftCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "files": obj.get("files"),
            "file_urls": obj.get("file_urls"),
            "allow_decline": obj.get("allow_decline") if obj.get("allow_decline") is not None else False,
            "attachments": [SubAttachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None,
            "cc_email_addresses": obj.get("cc_email_addresses"),
            "client_id": obj.get("client_id"),
            "custom_fields": [SubCustomField.from_dict(_item) for _item in obj["custom_fields"]] if obj.get("custom_fields") is not None else None,
            "field_options": SubFieldOptions.from_dict(obj["field_options"]) if obj.get("field_options") is not None else None,
            "form_field_groups": [SubFormFieldGroup.from_dict(_item) for _item in obj["form_field_groups"]] if obj.get("form_field_groups") is not None else None,
            "form_field_rules": [SubFormFieldRule.from_dict(_item) for _item in obj["form_field_rules"]] if obj.get("form_field_rules") is not None else None,
            "form_fields_per_document": [SubFormFieldsPerDocumentBase.from_dict(_item) for _item in obj["form_fields_per_document"]] if obj.get("form_fields_per_document") is not None else None,
            "hide_text_tags": obj.get("hide_text_tags") if obj.get("hide_text_tags") is not None else False,
            "message": obj.get("message"),
            "metadata": obj.get("metadata"),
            "show_progress_stepper": obj.get("show_progress_stepper") if obj.get("show_progress_stepper") is not None else True,
            "signers": [SubUnclaimedDraftSigner.from_dict(_item) for _item in obj["signers"]] if obj.get("signers") is not None else None,
            "signing_options": SubSigningOptions.from_dict(obj["signing_options"]) if obj.get("signing_options") is not None else None,
            "signing_redirect_url": obj.get("signing_redirect_url"),
            "subject": obj.get("subject"),
            "test_mode": obj.get("test_mode") if obj.get("test_mode") is not None else False,
            "use_preexisting_fields": obj.get("use_preexisting_fields") if obj.get("use_preexisting_fields") is not None else False,
            "use_text_tags": obj.get("use_text_tags") if obj.get("use_text_tags") is not None else False,
            "expires_at": obj.get("expires_at")
        })
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
            "files": "(List[io.IOBase],)",
            "file_urls": "(List[str],)",
            "allow_decline": "(bool,)",
            "attachments": "(List[SubAttachment],)",
            "cc_email_addresses": "(List[str],)",
            "client_id": "(str,)",
            "custom_fields": "(List[SubCustomField],)",
            "field_options": "(SubFieldOptions,)",
            "form_field_groups": "(List[SubFormFieldGroup],)",
            "form_field_rules": "(List[SubFormFieldRule],)",
            "form_fields_per_document": "(List[SubFormFieldsPerDocumentBase],)",
            "hide_text_tags": "(bool,)",
            "message": "(str,)",
            "metadata": "(Dict[str, object],)",
            "show_progress_stepper": "(bool,)",
            "signers": "(List[SubUnclaimedDraftSigner],)",
            "signing_options": "(SubSigningOptions,)",
            "signing_redirect_url": "(str,)",
            "subject": "(str,)",
            "test_mode": "(bool,)",
            "use_preexisting_fields": "(bool,)",
            "use_text_tags": "(bool,)",
            "expires_at": "(int,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "files",
            "file_urls",
            "attachments",
            "cc_email_addresses",
            "custom_fields",
            "form_field_groups",
            "form_field_rules",
            "form_fields_per_document",
            "signers",
        ]

