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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from dropbox_sign.models.sub_form_field_rule_action import SubFormFieldRuleAction
from dropbox_sign.models.sub_form_field_rule_trigger import SubFormFieldRuleTrigger
from typing import Optional, Set, Tuple
from typing_extensions import Self
import io
from pydantic import StrictBool
from typing import Union

class SubFormFieldRule(BaseModel):
    """
    SubFormFieldRule
    """ # noqa: E501
    id: StrictStr = Field(description="Must be unique across all defined rules.")
    trigger_operator: StrictStr = Field(description="Currently only `AND` is supported. Support for `OR` is being worked on.")
    triggers: Annotated[List[SubFormFieldRuleTrigger], Field(min_length=1, max_length=1)] = Field(description="An array of trigger definitions, the \"if this\" part of \"**if this**, then that\". Currently only a single trigger per rule is allowed.")
    actions: Annotated[List[SubFormFieldRuleAction], Field(min_length=1)] = Field(description="An array of action definitions, the \"then that\" part of \"if this, **then that**\". Any number of actions may be attached to a single rule.")
    __properties: ClassVar[List[str]] = ["id", "trigger_operator", "triggers", "actions"]

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
        """Create an instance of SubFormFieldRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item_triggers in self.triggers:
                if _item_triggers:
                    _items.append(_item_triggers.to_dict())
            _dict['triggers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubFormFieldRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "trigger_operator": obj.get("trigger_operator") if obj.get("trigger_operator") is not None else 'AND',
            "triggers": [SubFormFieldRuleTrigger.from_dict(_item) for _item in obj["triggers"]] if obj.get("triggers") is not None else None,
            "actions": [SubFormFieldRuleAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None
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
            "id": "(str,)",
            "trigger_operator": "(str,)",
            "triggers": "(List[SubFormFieldRuleTrigger],)",
            "actions": "(List[SubFormFieldRuleAction],)",
        }

    @classmethod
    def openapi_type_is_array(cls, property_name: str) -> bool:
        return property_name in [
            "triggers",
            "actions",
        ]

