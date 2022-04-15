"""
    HelloSign API

    HelloSign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from hellosign_sdk.model_utils import (  # noqa: F401
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
from hellosign_sdk.exceptions import ApiAttributeError


def lazy_import():
    from hellosign_sdk.model.sub_editor_options import SubEditorOptions
    from hellosign_sdk.model.sub_merge_field import SubMergeField
    globals()['SubEditorOptions'] = SubEditorOptions
    globals()['SubMergeField'] = SubMergeField


class EmbeddedEditUrlRequest(ModelNormal):
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
            'allow_edit_ccs': (bool,),  # noqa: E501
            'cc_roles': ([str],),  # noqa: E501
            'editor_options': (SubEditorOptions,),  # noqa: E501
            'force_signer_roles': (bool,),  # noqa: E501
            'force_subject_message': (bool,),  # noqa: E501
            'merge_fields': ([SubMergeField],),  # noqa: E501
            'preview_only': (bool,),  # noqa: E501
            'show_preview': (bool,),  # noqa: E501
            'show_progress_stepper': (bool,),  # noqa: E501
            'skip_signer_roles': (bool,),  # noqa: E501
            'skip_subject_message': (bool,),  # noqa: E501
            'test_mode': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_edit_ccs': 'allow_edit_ccs',  # noqa: E501
        'cc_roles': 'cc_roles',  # noqa: E501
        'editor_options': 'editor_options',  # noqa: E501
        'force_signer_roles': 'force_signer_roles',  # noqa: E501
        'force_subject_message': 'force_subject_message',  # noqa: E501
        'merge_fields': 'merge_fields',  # noqa: E501
        'preview_only': 'preview_only',  # noqa: E501
        'show_preview': 'show_preview',  # noqa: E501
        'show_progress_stepper': 'show_progress_stepper',  # noqa: E501
        'skip_signer_roles': 'skip_signer_roles',  # noqa: E501
        'skip_subject_message': 'skip_subject_message',  # noqa: E501
        'test_mode': 'test_mode',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EmbeddedEditUrlRequest - a model defined in OpenAPI

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
            allow_edit_ccs (bool): This allows the requester to enable/disable to add or change CC roles when editing the template.. [optional] if omitted the server will use the default value of False  # noqa: E501
            cc_roles ([str]): The CC roles that must be assigned when using the template to send a signature request. To remove all CC roles, pass in a single role with no name. For use in a POST request.. [optional]  # noqa: E501
            editor_options (SubEditorOptions): [optional]  # noqa: E501
            force_signer_roles (bool): Provide users the ability to review/edit the template signer roles.. [optional] if omitted the server will use the default value of False  # noqa: E501
            force_subject_message (bool): Provide users the ability to review/edit the template subject and message.. [optional] if omitted the server will use the default value of False  # noqa: E501
            merge_fields ([SubMergeField]): [optional]  # noqa: E501
            preview_only (bool): This allows the requester to enable the preview experience (i.e. does not allow the requester's end user to add any additional fields via the editor).  **Note**: This parameter overwrites `show_preview=true` (if set).. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_preview (bool): This allows the requester to enable the editor/preview experience.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_progress_stepper (bool): When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.. [optional] if omitted the server will use the default value of True  # noqa: E501
            skip_signer_roles (bool): If signer roles are already provided, the user will not be prompted to edit them.  **Note**: this parameter will be deprecated in May 2020 and skipping the signer roles screen will become the default behavior. To enforce showing the signer roles screen, use the `force_signer_roles` parameter.. [optional] if omitted the server will use the default value of False  # noqa: E501
            skip_subject_message (bool): If the subject and message has already been provided, the user will not be prompted to edit them.  **Note**: this parameter will be deprecated in May 2020 and skipping the subject message screen will become the default behavior. To enforce showing the subject message screen, use the `force_subject_message` parameter.. [optional] if omitted the server will use the default value of False  # noqa: E501
            test_mode (bool): Whether this is a test, locked templates will only be available for editing if this is set to `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
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
        """EmbeddedEditUrlRequest - a model defined in OpenAPI

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
            allow_edit_ccs (bool): This allows the requester to enable/disable to add or change CC roles when editing the template.. [optional] if omitted the server will use the default value of False  # noqa: E501
            cc_roles ([str]): The CC roles that must be assigned when using the template to send a signature request. To remove all CC roles, pass in a single role with no name. For use in a POST request.. [optional]  # noqa: E501
            editor_options (SubEditorOptions): [optional]  # noqa: E501
            force_signer_roles (bool): Provide users the ability to review/edit the template signer roles.. [optional] if omitted the server will use the default value of False  # noqa: E501
            force_subject_message (bool): Provide users the ability to review/edit the template subject and message.. [optional] if omitted the server will use the default value of False  # noqa: E501
            merge_fields ([SubMergeField]): [optional]  # noqa: E501
            preview_only (bool): This allows the requester to enable the preview experience (i.e. does not allow the requester's end user to add any additional fields via the editor).  **Note**: This parameter overwrites `show_preview=true` (if set).. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_preview (bool): This allows the requester to enable the editor/preview experience.. [optional] if omitted the server will use the default value of False  # noqa: E501
            show_progress_stepper (bool): When only one step remains in the signature request process and this parameter is set to `false` then the progress stepper will be hidden.. [optional] if omitted the server will use the default value of True  # noqa: E501
            skip_signer_roles (bool): If signer roles are already provided, the user will not be prompted to edit them.  **Note**: this parameter will be deprecated in May 2020 and skipping the signer roles screen will become the default behavior. To enforce showing the signer roles screen, use the `force_signer_roles` parameter.. [optional] if omitted the server will use the default value of False  # noqa: E501
            skip_subject_message (bool): If the subject and message has already been provided, the user will not be prompted to edit them.  **Note**: this parameter will be deprecated in May 2020 and skipping the subject message screen will become the default behavior. To enforce showing the subject message screen, use the `force_subject_message` parameter.. [optional] if omitted the server will use the default value of False  # noqa: E501
            test_mode (bool): Whether this is a test, locked templates will only be available for editing if this is set to `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
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
