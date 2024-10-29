from pprint import pprint

from dropbox_sign import ApiClient, ApiException, Configuration, apis

configuration = Configuration(
    # Configure HTTP basic authorization: api_key
    username="YOUR_API_KEY",
)

with ApiClient(configuration) as api_client:
    fax_api = apis.FaxApi(api_client)

    fax_id = "fa5c8a0b0f492d768749333ad6fcc214c111e967"

    try:
        response = fax_api.fax_get(fax_id)
        pprint(response)
    except ApiException as e:
        print("Exception when calling Dropbox Sign API: %s\n" % e)