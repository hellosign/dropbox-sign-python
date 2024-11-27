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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dropbox_sign.models.signature_request_response_attachment import (
    SignatureRequestResponseAttachment,
)
from dropbox_sign.models.signature_request_response_custom_field_base import (
    SignatureRequestResponseCustomFieldBase,
)
from dropbox_sign.models.signature_request_response_data_base import (
    SignatureRequestResponseDataBase,
)
from dropbox_sign.models.signature_request_response_signatures import (
    SignatureRequestResponseSignatures,
)
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union


class BulkSendJobGetResponseSignatureRequests(BaseModel):
    """
    BulkSendJobGetResponseSignatureRequests
    """  # noqa: E501

    test_mode: Optional[StrictBool] = Field(
        default=False,
        description="Whether this is a test signature request. Test requests have no legal value. Defaults to `false`.",
    )
    signature_request_id: Optional[StrictStr] = Field(
        default=None, description="The id of the SignatureRequest."
    )
    requester_email_address: Optional[StrictStr] = Field(
        default=None,
        description="The email address of the initiator of the SignatureRequest.",
    )
    title: Optional[StrictStr] = Field(
        default=None,
        description="The title the specified Account uses for the SignatureRequest.",
    )
    original_title: Optional[StrictStr] = Field(
        default=None, description="Default Label for account."
    )
    subject: Optional[StrictStr] = Field(
        default=None,
        description="The subject in the email that was initially sent to the signers.",
    )
    message: Optional[StrictStr] = Field(
        default=None,
        description="The custom message in the email that was initially sent to the signers.",
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None, description="The metadata attached to the signature request."
    )
    created_at: Optional[StrictInt] = Field(
        default=None, description="Time the signature request was created."
    )
    expires_at: Optional[StrictInt] = Field(
        default=None,
        description="The time when the signature request will expire unsigned signatures. See [Signature Request Expiration Date](https://developers.hellosign.com/docs/signature-request/expiration/) for details.",
    )
    is_complete: Optional[StrictBool] = Field(
        default=None,
        description="Whether or not the SignatureRequest has been fully executed by all signers.",
    )
    is_declined: Optional[StrictBool] = Field(
        default=None,
        description="Whether or not the SignatureRequest has been declined by a signer.",
    )
    has_error: Optional[StrictBool] = Field(
        default=None,
        description="Whether or not an error occurred (either during the creation of the SignatureRequest or during one of the signings).",
    )
    files_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL where a copy of the request's documents can be downloaded.",
    )
    signing_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL where a signer, after authenticating, can sign the documents. This should only be used by users with existing Dropbox Sign accounts as they will be required to log in before signing.",
    )
    details_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL where the requester and the signers can view the current status of the SignatureRequest.",
    )
    cc_email_addresses: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of email addresses that were CCed on the SignatureRequest. They will receive a copy of the final PDF once all the signers have signed.",
    )
    signing_redirect_url: Optional[StrictStr] = Field(
        default=None,
        description="The URL you want the signer redirected to after they successfully sign.",
    )
    final_copy_uri: Optional[StrictStr] = Field(
        default=None,
        description="The path where the completed document can be downloaded",
    )
    template_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="Templates IDs used in this SignatureRequest (if any).",
    )
    custom_fields: Optional[List[SignatureRequestResponseCustomFieldBase]] = Field(
        default=None,
        description="An array of Custom Field objects containing the name and type of each custom field.  * Text Field uses `SignatureRequestResponseCustomFieldText` * Checkbox Field uses `SignatureRequestResponseCustomFieldCheckbox`",
    )
    attachments: Optional[List[SignatureRequestResponseAttachment]] = Field(
        default=None, description="Signer attachments."
    )
    response_data: Optional[List[SignatureRequestResponseDataBase]] = Field(
        default=None,
        description="An array of form field objects containing the name, value, and type of each textbox or checkmark field filled in by the signers.",
    )
    signatures: Optional[List[SignatureRequestResponseSignatures]] = Field(
        default=None, description="An array of signature objects, 1 for each signer."
    )
    bulk_send_job_id: Optional[StrictStr] = Field(
        default=None, description="The id of the BulkSendJob."
    )
    __properties: ClassVar[List[str]] = [
        "test_mode",
        "signature_request_id",
        "requester_email_address",
        "title",
        "original_title",
        "subject",
        "message",
        "metadata",
        "created_at",
        "expires_at",
        "is_complete",
        "is_declined",
        "has_error",
        "files_url",
        "signing_url",
        "details_url",
        "cc_email_addresses",
        "signing_redirect_url",
        "final_copy_uri",
        "template_ids",
        "custom_fields",
        "attachments",
        "response_data",
        "signatures",
        "bulk_send_job_id",
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
        """Create an instance of BulkSendJobGetResponseSignatureRequests from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item_custom_fields in self.custom_fields:
                if _item_custom_fields:
                    _items.append(_item_custom_fields.to_dict())
            _dict["custom_fields"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item_attachments in self.attachments:
                if _item_attachments:
                    _items.append(_item_attachments.to_dict())
            _dict["attachments"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in response_data (list)
        _items = []
        if self.response_data:
            for _item_response_data in self.response_data:
                if _item_response_data:
                    _items.append(_item_response_data.to_dict())
            _dict["response_data"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in signatures (list)
        _items = []
        if self.signatures:
            for _item_signatures in self.signatures:
                if _item_signatures:
                    _items.append(_item_signatures.to_dict())
            _dict["signatures"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BulkSendJobGetResponseSignatureRequests from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "test_mode": (
                    obj.get("test_mode") if obj.get("test_mode") is not None else False
                ),
                "signature_request_id": obj.get("signature_request_id"),
                "requester_email_address": obj.get("requester_email_address"),
                "title": obj.get("title"),
                "original_title": obj.get("original_title"),
                "subject": obj.get("subject"),
                "message": obj.get("message"),
                "metadata": obj.get("metadata"),
                "created_at": obj.get("created_at"),
                "expires_at": obj.get("expires_at"),
                "is_complete": obj.get("is_complete"),
                "is_declined": obj.get("is_declined"),
                "has_error": obj.get("has_error"),
                "files_url": obj.get("files_url"),
                "signing_url": obj.get("signing_url"),
                "details_url": obj.get("details_url"),
                "cc_email_addresses": obj.get("cc_email_addresses"),
                "signing_redirect_url": obj.get("signing_redirect_url"),
                "final_copy_uri": obj.get("final_copy_uri"),
                "template_ids": obj.get("template_ids"),
                "custom_fields": (
                    [
                        SignatureRequestResponseCustomFieldBase.from_dict(_item)
                        for _item in obj["custom_fields"]
                    ]
                    if obj.get("custom_fields") is not None
                    else None
                ),
                "attachments": (
                    [
                        SignatureRequestResponseAttachment.from_dict(_item)
                        for _item in obj["attachments"]
                    ]
                    if obj.get("attachments") is not None
                    else None
                ),
                "response_data": (
                    [
                        SignatureRequestResponseDataBase.from_dict(_item)
                        for _item in obj["response_data"]
                    ]
                    if obj.get("response_data") is not None
                    else None
                ),
                "signatures": (
                    [
                        SignatureRequestResponseSignatures.from_dict(_item)
                        for _item in obj["signatures"]
                    ]
                    if obj.get("signatures") is not None
                    else None
                ),
                "bulk_send_job_id": obj.get("bulk_send_job_id"),
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
            "test_mode": "(bool,)",
            "signature_request_id": "(str,)",
            "requester_email_address": "(str,)",
            "title": "(str,)",
            "original_title": "(str,)",
            "subject": "(str,)",
            "message": "(str,)",
            "metadata": "(Dict[str, object],)",
            "created_at": "(int,)",
            "expires_at": "(int,)",
            "is_complete": "(bool,)",
            "is_declined": "(bool,)",
            "has_error": "(bool,)",
            "files_url": "(str,)",
            "signing_url": "(str,)",
            "details_url": "(str,)",
            "cc_email_addresses": "(List[str],)",
            "signing_redirect_url": "(str,)",
            "final_copy_uri": "(str,)",
            "template_ids": "(List[str],)",
            "custom_fields": "(List[SignatureRequestResponseCustomFieldBase],)",
            "attachments": "(List[SignatureRequestResponseAttachment],)",
            "response_data": "(List[SignatureRequestResponseDataBase],)",
            "signatures": "(List[SignatureRequestResponseSignatures],)",
            "bulk_send_job_id": "(str,)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "cc_email_addresses",
            "template_ids",
            "custom_fields",
            "attachments",
            "response_data",
            "signatures",
        ]
