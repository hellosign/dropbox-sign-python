# ```hellosign_sdk.AccountApi```

All URIs are relative to *https://api.hellosign.com/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[```account_create```](AccountApi.md#account_create) | ```POST /account/create``` | Signs up for a new HelloSign Account.|
|[```account_get```](AccountApi.md#account_get) | ```GET /account``` | Returns your Account settings.|
|[```account_update```](AccountApi.md#account_update) | ```PUT /account``` | Updates your Account&#39;s settings.|
|[```account_verify```](AccountApi.md#account_verify) | ```POST /account/verify``` | Verify whether a HelloSign Account exists.|


# ```account_create```
> ```AccountCreateResponse account_create(account_create_request)```

Signs up for a new HelloSign Account.

Creates a new HelloSign Account that is associated with the specified `email_address`.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.AccountApi(api_client)

    data = models.AccountCreateRequest(
        email_address="newuser@hellosign.com",
    )

    try:
        response = api.account_create(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `account_create_request` | [**AccountCreateRequest**](AccountCreateRequest.md) |  |  |

### Return type

[**AccountCreateResponse**](AccountCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | failed operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```account_get```
> ```AccountGetResponse account_get()```

Returns your Account settings.

Returns the properties and settings of your Account.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.AccountApi(api_client)

    try:
        response = api.account_get()
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountGetResponse**](AccountGetResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | failed operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```account_update```
> ```AccountGetResponse account_update(account_update_request)```

Updates your Account's settings.

Updates the properties and settings of your Account.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.AccountApi(api_client)

    data = models.AccountUpdateRequest(
        callback_url="https://www.example.com/callback",
    )

    try:
        response = api.account_update(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `account_update_request` | [**AccountUpdateRequest**](AccountUpdateRequest.md) |  |  |

### Return type

[**AccountGetResponse**](AccountGetResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | failed operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# ```account_verify```
> ```AccountVerifyResponse account_verify(account_verify_request)```

Verify whether a HelloSign Account exists.

Verifies whether an HelloSign Account exists for the given email address.  **NOTE** This method is restricted to paid API users.

### Example

* Basic Authentication (api_key):
* Bearer (JWT) Authentication (oauth2):

```python
from pprint import pprint

from hellosign_sdk import \
    ApiClient, ApiException, Configuration, apis, models

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",

    # or, configure Bearer (JWT) authorization: oauth2
    # access_token="YOUR_ACCESS_TOKEN",
)

with ApiClient(configuration) as api_client:
    api = apis.AccountApi(api_client)

    data = models.AccountVerifyRequest(
        email_address="some_user@hellosign.com",
    )

    try:
        response = api.account_verify(data)
        pprint(response)
    except ApiException as e:
        print("Exception when calling HelloSign API: %s\n" % e)

```


### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| `account_verify_request` | [**AccountVerifyRequest**](AccountVerifyRequest.md) |  |  |

### Return type

[**AccountVerifyResponse**](AccountVerifyResponse.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | failed operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
