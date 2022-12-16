"""
    Dropbox Sign API

    Dropbox Sign v3 API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Contact: apisupport@hellosign.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from hellosign_sdk.api_client import ApiClient, ApiException, Endpoint as _Endpoint
from hellosign_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from hellosign_sdk.model.error_response import ErrorResponse
from hellosign_sdk.model.report_create_request import ReportCreateRequest
from hellosign_sdk.model.report_create_response import ReportCreateResponse


class ReportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.report_create_endpoint = _Endpoint(
            settings={
                'response_type': (ReportCreateResponse,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/report/create',
                'operation_id': 'report_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'report_create_request',
                ],
                'required': [
                    'report_create_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'report_create_request':
                        (ReportCreateRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'report_create_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def report_create(
        self,
        report_create_request,
        **kwargs
    ):
        """Create Report  # noqa: E501

        Request the creation of one or more report(s).  When the report(s) have been generated, you will receive an email (one per requested report type) containing a link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and `start_date` must not be more than 10 years in the past.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.report_create(report_create_request, async_req=True)
        >>> result = thread.get()

        Args:
            report_create_request (ReportCreateRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ReportCreateResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['report_create_request'] = \
            report_create_request
        try:
            return self.report_create_endpoint.call_with_http_info(**kwargs)
        except ApiException as e:
            if e.status == 200:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[ReportCreateResponse],
                    _check_type=True,
                )

                raise e
            range_code = "4XX"[0]
            range_code_left = int(f"{range_code}00")
            range_code_right = int(f"{range_code}99")

            if range_code_left <= e.status <= range_code_right:
                e.body = self.api_client.deserialize(
                    response=type('obj_dict', (object,), {'data': e.body}),
                    response_type=[ErrorResponse],
                    _check_type=True,
                )

                raise e

