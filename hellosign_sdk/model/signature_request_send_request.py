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
    from hellosign_sdk.model.sub_attachment import SubAttachment
    from hellosign_sdk.model.sub_custom_field import SubCustomField
    from hellosign_sdk.model.sub_field_options import SubFieldOptions
    from hellosign_sdk.model.sub_form_field_group import SubFormFieldGroup
    from hellosign_sdk.model.sub_form_field_rule import SubFormFieldRule
    from hellosign_sdk.model.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase
    from hellosign_sdk.model.sub_signature_request_signer import SubSignatureRequestSigner
    from hellosign_sdk.model.sub_signing_options import SubSigningOptions
    globals()['SubAttachment'] = SubAttachment
    globals()['SubCustomField'] = SubCustomField
    globals()['SubFieldOptions'] = SubFieldOptions
    globals()['SubFormFieldGroup'] = SubFormFieldGroup
    globals()['SubFormFieldRule'] = SubFormFieldRule
    globals()['SubFormFieldsPerDocumentBase'] = SubFormFieldsPerDocumentBase
    globals()['SubSignatureRequestSigner'] = SubSignatureRequestSigner
    globals()['SubSigningOptions'] = SubSigningOptions


class SignatureRequestSendRequest(ModelNormal):
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
        ('message',): {
            'max_length': 5000,
        },
        ('metadata',): {
        },
        ('subject',): {
            'max_length': 255,
        },
        ('title',): {
            'max_length': 255,
        },
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
            'signers': ([SubSignatureRequestSigner],),  # noqa: E501
            'file': ([file_type],),  # noqa: E501
            'file_url': ([str],),  # noqa: E501
            'allow_decline': (bool,),  # noqa: E501
            'allow_reassign': (bool,),  # noqa: E501
            'attachments': ([SubAttachment],),  # noqa: E501
            'cc_email_addresses': ([str],),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'custom_fields': ([SubCustomField],),  # noqa: E501
            'field_options': (SubFieldOptions,),  # noqa: E501
            'form_field_groups': ([SubFormFieldGroup],),  # noqa: E501
            'form_field_rules': ([SubFormFieldRule],),  # noqa: E501
            'form_fields_per_document': ([[SubFormFieldsPerDocumentBase]],),  # noqa: E501
            'hide_text_tags': (bool,),  # noqa: E501
            'message': (str,),  # noqa: E501
            'metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'signing_options': (SubSigningOptions,),  # noqa: E501
            'signing_redirect_url': (str,),  # noqa: E501
            'subject': (str,),  # noqa: E501
            'test_mode': (bool,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'use_text_tags': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'signers': 'signers',  # noqa: E501
        'file': 'file',  # noqa: E501
        'file_url': 'file_url',  # noqa: E501
        'allow_decline': 'allow_decline',  # noqa: E501
        'allow_reassign': 'allow_reassign',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'cc_email_addresses': 'cc_email_addresses',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'custom_fields': 'custom_fields',  # noqa: E501
        'field_options': 'field_options',  # noqa: E501
        'form_field_groups': 'form_field_groups',  # noqa: E501
        'form_field_rules': 'form_field_rules',  # noqa: E501
        'form_fields_per_document': 'form_fields_per_document',  # noqa: E501
        'hide_text_tags': 'hide_text_tags',  # noqa: E501
        'message': 'message',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'signing_options': 'signing_options',  # noqa: E501
        'signing_redirect_url': 'signing_redirect_url',  # noqa: E501
        'subject': 'subject',  # noqa: E501
        'test_mode': 'test_mode',  # noqa: E501
        'title': 'title',  # noqa: E501
        'use_text_tags': 'use_text_tags',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, signers, *args, **kwargs):  # noqa: E501
        """SignatureRequestSendRequest - a model defined in OpenAPI

        Args:
            signers ([SubSignatureRequestSigner]): Add Signers to your Signature Request.

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
            file ([file_type]): **file** or **file_url** is required, but not both.  Use `file[]` to indicate the uploaded file(s) to send for signature.  Currently we only support use of either the `file[]` parameter or `file_url[]` parameter, not both.. [optional]  # noqa: E501
            file_url ([str]): **file_url** or **file** is required, but not both.  Use `file_url[]` to have HelloSign download the file(s) to send for signature.  Currently we only support use of either the `file[]` parameter or `file_url[]` parameter, not both.. [optional]  # noqa: E501
            allow_decline (bool): Allows signers to decline to sign a document if `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            allow_reassign (bool): Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.  **Note**: Only available for Gold plan and higher.. [optional] if omitted the server will use the default value of False  # noqa: E501
            attachments ([SubAttachment]): [optional]  # noqa: E501
            cc_email_addresses ([str]): The email addresses that should be CCed.. [optional]  # noqa: E501
            client_id (str): The client ID of the ApiApp you want to associate with this request.. [optional]  # noqa: E501
            custom_fields ([SubCustomField]): An array defining values and options for custom fields. Required when defining pre-set values in `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro).. [optional]  # noqa: E501
            field_options (SubFieldOptions): [optional]  # noqa: E501
            form_field_groups ([SubFormFieldGroup]): Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.. [optional]  # noqa: E501
            form_field_rules ([SubFormFieldRule]): Conditional Logic rules for fields defined in `form_fields_per_document`.. [optional]  # noqa: E501
            form_fields_per_document ([[SubFormFieldsPerDocumentBase]]): The fields that should appear on the document, expressed as a 2-dimensional JSON array serialized to a string. The main array represents documents, with each containing an array of form fields. One document array is required for each file provided by the `file[]` parameter. In the case of a file with no fields, an empty list must be specified.  **NOTE**: Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](https://app.hellosign.com/api/reference#FormFieldsPerDocument) for these field types.  * Text Field use `SubFormFieldsPerDocumentText` * Dropdown Field use `SubFormFieldsPerDocumentDropdown` * Hyperlink Field use `SubFormFieldsPerDocumentHyperlink` * Checkbox Field use `SubFormFieldsPerDocumentCheckbox` * Radio Field use `SubFormFieldsPerDocumentRadio` * Signature Field use `SubFormFieldsPerDocumentSignature` * Date Signed Field use `SubFormFieldsPerDocumentDateSigned` * Initials Field use `SubFormFieldsPerDocumentInitials` * Text Merge Field use `SubFormFieldsPerDocumentTextMerge` * Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`. [optional]  # noqa: E501
            hide_text_tags (bool): Send with a value of `true` if you wish to enable automatic Text Tag removal. Defaults to `false`. When using Text Tags it is preferred that you set this to `false` and hide your tags with white text or something similar because the automatic removal system can cause unwanted clipping. See the [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) walkthrough for more details.. [optional] if omitted the server will use the default value of False  # noqa: E501
            message (str): The custom message in the email that will be sent to the signers.. [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.  Each request can include up to 10 metadata keys, with key names up to 40 characters long and values up to 1000 characters long.. [optional]  # noqa: E501
            signing_options (SubSigningOptions): [optional]  # noqa: E501
            signing_redirect_url (str): The URL you want signers redirected to after they successfully sign.. [optional]  # noqa: E501
            subject (str): The subject in the email that will be sent to the signers.. [optional]  # noqa: E501
            test_mode (bool): Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            title (str): The title you want to assign to the SignatureRequest.. [optional]  # noqa: E501
            use_text_tags (bool): Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
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

        self.signers = signers
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
    def __init__(self, signers, *args, **kwargs):  # noqa: E501
        """SignatureRequestSendRequest - a model defined in OpenAPI

        Args:
            signers ([SubSignatureRequestSigner]): Add Signers to your Signature Request.

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
            file ([file_type]): **file** or **file_url** is required, but not both.  Use `file[]` to indicate the uploaded file(s) to send for signature.  Currently we only support use of either the `file[]` parameter or `file_url[]` parameter, not both.. [optional]  # noqa: E501
            file_url ([str]): **file_url** or **file** is required, but not both.  Use `file_url[]` to have HelloSign download the file(s) to send for signature.  Currently we only support use of either the `file[]` parameter or `file_url[]` parameter, not both.. [optional]  # noqa: E501
            allow_decline (bool): Allows signers to decline to sign a document if `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            allow_reassign (bool): Allows signers to reassign their signature requests to other signers if set to `true`. Defaults to `false`.  **Note**: Only available for Gold plan and higher.. [optional] if omitted the server will use the default value of False  # noqa: E501
            attachments ([SubAttachment]): [optional]  # noqa: E501
            cc_email_addresses ([str]): The email addresses that should be CCed.. [optional]  # noqa: E501
            client_id (str): The client ID of the ApiApp you want to associate with this request.. [optional]  # noqa: E501
            custom_fields ([SubCustomField]): An array defining values and options for custom fields. Required when defining pre-set values in `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro).. [optional]  # noqa: E501
            field_options (SubFieldOptions): [optional]  # noqa: E501
            form_field_groups ([SubFormFieldGroup]): Group information for fields defined in `form_fields_per_document`. String-indexed JSON array with `group_label` and `requirement` keys. `form_fields_per_document` must contain fields referencing a group defined in `form_field_groups`.. [optional]  # noqa: E501
            form_field_rules ([SubFormFieldRule]): Conditional Logic rules for fields defined in `form_fields_per_document`.. [optional]  # noqa: E501
            form_fields_per_document ([[SubFormFieldsPerDocumentBase]]): The fields that should appear on the document, expressed as a 2-dimensional JSON array serialized to a string. The main array represents documents, with each containing an array of form fields. One document array is required for each file provided by the `file[]` parameter. In the case of a file with no fields, an empty list must be specified.  **NOTE**: Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out the list of [additional parameters](https://app.hellosign.com/api/reference#FormFieldsPerDocument) for these field types.  * Text Field use `SubFormFieldsPerDocumentText` * Dropdown Field use `SubFormFieldsPerDocumentDropdown` * Hyperlink Field use `SubFormFieldsPerDocumentHyperlink` * Checkbox Field use `SubFormFieldsPerDocumentCheckbox` * Radio Field use `SubFormFieldsPerDocumentRadio` * Signature Field use `SubFormFieldsPerDocumentSignature` * Date Signed Field use `SubFormFieldsPerDocumentDateSigned` * Initials Field use `SubFormFieldsPerDocumentInitials` * Text Merge Field use `SubFormFieldsPerDocumentTextMerge` * Checkbox Merge Field use `SubFormFieldsPerDocumentCheckboxMerge`. [optional]  # noqa: E501
            hide_text_tags (bool): Send with a value of `true` if you wish to enable automatic Text Tag removal. Defaults to `false`. When using Text Tags it is preferred that you set this to `false` and hide your tags with white text or something similar because the automatic removal system can cause unwanted clipping. See the [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) walkthrough for more details.. [optional] if omitted the server will use the default value of False  # noqa: E501
            message (str): The custom message in the email that will be sent to the signers.. [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer's order number for look up when receiving events for the signature request.  Each request can include up to 10 metadata keys, with key names up to 40 characters long and values up to 1000 characters long.. [optional]  # noqa: E501
            signing_options (SubSigningOptions): [optional]  # noqa: E501
            signing_redirect_url (str): The URL you want signers redirected to after they successfully sign.. [optional]  # noqa: E501
            subject (str): The subject in the email that will be sent to the signers.. [optional]  # noqa: E501
            test_mode (bool): Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
            title (str): The title you want to assign to the SignatureRequest.. [optional]  # noqa: E501
            use_text_tags (bool): Send with a value of `true` if you wish to enable [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) parsing in your document. Defaults to disabled, or `false`.. [optional] if omitted the server will use the default value of False  # noqa: E501
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

        self.signers = signers
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
