"""
    Dropbox Sign API

    Dropbox Sign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Dict, Union
import json  # noqa: F401
import re  # noqa: F401
import sys  # noqa: F401

from dropbox_sign import ApiClient
from dropbox_sign.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from dropbox_sign.exceptions import ApiAttributeError
if TYPE_CHECKING:
    from dropbox_sign.model.template_response_field_avg_text_length import TemplateResponseFieldAvgTextLength


def lazy_import():
    from dropbox_sign.model.template_response_field_avg_text_length import TemplateResponseFieldAvgTextLength
    globals()['TemplateResponseFieldAvgTextLength'] = TemplateResponseFieldAvgTextLength


class TemplateResponseCustomField(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('type',): {
            'TEXT': "text",
            'CHECKBOX': "checkbox",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'name': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'x': (int,),  # noqa: E501
            'y': (int,),  # noqa: E501
            'width': (int,),  # noqa: E501
            'height': (int,),  # noqa: E501
            'required': (bool,),  # noqa: E501
            'api_id': (str,),  # noqa: E501
            'group': (str, none_type,),  # noqa: E501
            'avg_text_length': (TemplateResponseFieldAvgTextLength,),  # noqa: E501
            'is_multiline': (bool, none_type,),  # noqa: E501
            'original_font_size': (int, none_type,),  # noqa: E501
            'font_family': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    @staticmethod
    def init(data: any) -> TemplateResponseCustomField:
        """
        Attempt to instantiate and hydrate a new instance of this class
        """
        try:
            obj_data = json.dumps(data)
        except TypeError:
            obj_data = data

        return ApiClient().deserialize(
            response=type('obj_dict', (object,), {'data': obj_data}),
            response_type=[TemplateResponseCustomField],
            _check_type=True,
        )

    attribute_map = {
        'name': 'name',  # noqa: E501
        'type': 'type',  # noqa: E501
        'x': 'x',  # noqa: E501
        'y': 'y',  # noqa: E501
        'width': 'width',  # noqa: E501
        'height': 'height',  # noqa: E501
        'required': 'required',  # noqa: E501
        'api_id': 'api_id',  # noqa: E501
        'group': 'group',  # noqa: E501
        'avg_text_length': 'avg_text_length',  # noqa: E501
        'is_multiline': 'isMultiline',  # noqa: E501
        'original_font_size': 'originalFontSize',  # noqa: E501
        'font_family': 'fontFamily',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @property
    def name(self) -> str:
        return self.get("name")

    @name.setter
    def name(self, value: str):
        setattr(self, "name", value)

    @property
    def type(self) -> str:
        return self.get("type")

    @type.setter
    def type(self, value: str):
        setattr(self, "type", value)

    @property
    def x(self) -> int:
        return self.get("x")

    @x.setter
    def x(self, value: int):
        setattr(self, "x", value)

    @property
    def y(self) -> int:
        return self.get("y")

    @y.setter
    def y(self, value: int):
        setattr(self, "y", value)

    @property
    def width(self) -> int:
        return self.get("width")

    @width.setter
    def width(self, value: int):
        setattr(self, "width", value)

    @property
    def height(self) -> int:
        return self.get("height")

    @height.setter
    def height(self, value: int):
        setattr(self, "height", value)

    @property
    def required(self) -> bool:
        return self.get("required")

    @required.setter
    def required(self, value: bool):
        setattr(self, "required", value)

    @property
    def api_id(self) -> str:
        return self.get("api_id")

    @api_id.setter
    def api_id(self, value: str):
        setattr(self, "api_id", value)

    @property
    def group(self) -> Optional[str]:
        return self.get("group")

    @group.setter
    def group(self, value: Optional[str]):
        setattr(self, "group", value)

    @property
    def avg_text_length(self) -> TemplateResponseFieldAvgTextLength:
        return self.get("avg_text_length")

    @avg_text_length.setter
    def avg_text_length(self, value: TemplateResponseFieldAvgTextLength):
        setattr(self, "avg_text_length", value)

    @property
    def is_multiline(self) -> Optional[bool]:
        return self.get("is_multiline")

    @is_multiline.setter
    def is_multiline(self, value: Optional[bool]):
        setattr(self, "is_multiline", value)

    @property
    def original_font_size(self) -> Optional[int]:
        return self.get("original_font_size")

    @original_font_size.setter
    def original_font_size(self, value: Optional[int]):
        setattr(self, "original_font_size", value)

    @property
    def font_family(self) -> Optional[str]:
        return self.get("font_family")

    @font_family.setter
    def font_family(self, value: Optional[str]):
        setattr(self, "font_family", value)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TemplateResponseCustomField - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): The name of the Custom Field.. [optional]  # noqa: E501
            type (str): The type of this Custom Field. Only `text` and `checkbox` are currently supported.. [optional]  # noqa: E501
            x (int): The horizontal offset in pixels for this form field.. [optional]  # noqa: E501
            y (int): The vertical offset in pixels for this form field.. [optional]  # noqa: E501
            width (int): The width in pixels of this form field.. [optional]  # noqa: E501
            height (int): The height in pixels of this form field.. [optional]  # noqa: E501
            required (bool): Boolean showing whether or not this field is required.. [optional]  # noqa: E501
            api_id (str): The unique ID for this field.. [optional]  # noqa: E501
            group (str, none_type): The name of the group this field is in. If this field is not a group, this defaults to `null`.. [optional]  # noqa: E501
            avg_text_length (TemplateResponseFieldAvgTextLength): [optional]  # noqa: E501
            is_multiline (bool, none_type): Whether this form field is multiline text.. [optional]  # noqa: E501
            original_font_size (int, none_type): Original font size used in this form field's text.. [optional]  # noqa: E501
            font_family (str, none_type): Font family used in this form field's text.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TemplateResponseCustomField - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): The name of the Custom Field.. [optional]  # noqa: E501
            type (str): The type of this Custom Field. Only `text` and `checkbox` are currently supported.. [optional]  # noqa: E501
            x (int): The horizontal offset in pixels for this form field.. [optional]  # noqa: E501
            y (int): The vertical offset in pixels for this form field.. [optional]  # noqa: E501
            width (int): The width in pixels of this form field.. [optional]  # noqa: E501
            height (int): The height in pixels of this form field.. [optional]  # noqa: E501
            required (bool): Boolean showing whether or not this field is required.. [optional]  # noqa: E501
            api_id (str): The unique ID for this field.. [optional]  # noqa: E501
            group (str, none_type): The name of the group this field is in. If this field is not a group, this defaults to `null`.. [optional]  # noqa: E501
            avg_text_length (TemplateResponseFieldAvgTextLength): [optional]  # noqa: E501
            is_multiline (bool, none_type): Whether this form field is multiline text.. [optional]  # noqa: E501
            original_font_size (int, none_type): Original font size used in this form field's text.. [optional]  # noqa: E501
            font_family (str, none_type): Font family used in this form field's text.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
