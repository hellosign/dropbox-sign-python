# SignatureRequestBulkSendWithTemplateRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
| `template_ids`<sup>*_required_</sup> | ```List[str]``` |  Use `template_ids` to create a SignatureRequest from one or more templates, in the order in which the template will be used.  |  |
| `signer_file` | ```io.IOBase``` |  `signer_file` is a CSV file defining values and options for signer fields. Required unless a `signer_list` is used, you may not use both. The CSV can have the following columns:<br><br>- `name`: the name of the signer filling the role of RoleName - `email_address`: email address of the signer filling the role of RoleName - `pin`: the 4- to 12-character access code that will secure this signer&#39;s signature page (optional) - `sms_phone_number`: An E.164 formatted phone number that will receive a code via SMS to access this signer&#39;s signature page. (optional)<br><br>    By using the feature, you agree you are responsible for obtaining a signer&#39;s consent to receive text messages from Dropbox Sign related to this signature request and confirm you have obtained such consent from all signers prior to enabling SMS delivery for this signature request. [Learn more](https://faq.hellosign.com/hc/en-us/articles/15815316468877-Dropbox-Sign-SMS-tools-add-on).<br><br>    **NOTE:** Not available in test mode and requires a Standard plan or higher. - `*_field`: any column with a _field&quot; suffix will be treated as a custom field (optional)<br><br>    You may only specify field values here, any other options should be set in the custom_fields request parameter.<br><br>Example CSV:<br><br>``` name, email_address, pin, company_field George, george@example.com, d79a3td, ABC Corp Mary, mary@example.com, gd9as5b, 123 LLC ```  |  |
| `signer_list` | [```List[SubBulkSignerList]```](SubBulkSignerList.md) |  `signer_list` is an array defining values and options for signer fields. Required unless a `signer_file` is used, you may not use both.  |  |
| `allow_decline` | ```bool``` |  Allows signers to decline to sign a document if `true`. Defaults to `false`.  |  [default to False] |
| `ccs` | [```List[SubCC]```](SubCC.md) |  Add CC email recipients. Required when a CC role exists for the Template.  |  |
| `client_id` | ```str``` |  The client id of the API App you want to associate with this request. Used to apply the branding and callback url defined for the app.  |  |
| `custom_fields` | [```List[SubCustomField]```](SubCustomField.md) |  When used together with merge fields, `custom_fields` allows users to add pre-filled data to their signature requests.<br><br>Pre-filled data can be used with &quot;send-once&quot; signature requests by adding merge fields with `form_fields_per_document` or [Text Tags](https://app.hellosign.com/api/textTagsWalkthrough#TextTagIntro) while passing values back with `custom_fields` together in one API call.<br><br>For using pre-filled on repeatable signature requests, merge fields are added to templates in the Dropbox Sign UI or by calling [/template/create_embedded_draft](/api/reference/operation/templateCreateEmbeddedDraft) and then passing `custom_fields` on subsequent signature requests referencing that template.  |  |
| `message` | ```str``` |  The custom message in the email that will be sent to the signers.  |  |
| `metadata` | ```Dict[str, object]``` |  Key-value data that should be attached to the signature request. This metadata is included in all API responses and events involving the signature request. For example, use the metadata field to store a signer&#39;s order number for look up when receiving events for the signature request.<br><br>Each request can include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and values up to 1000 characters long.  |  |
| `signing_redirect_url` | ```str``` |  The URL you want signers redirected to after they successfully sign.  |  |
| `subject` | ```str``` |  The subject in the email that will be sent to the signers.  |  |
| `test_mode` | ```bool``` |  Whether this is a test, the signature request will not be legally binding if set to `true`. Defaults to `false`.  |  [default to False] |
| `title` | ```str``` |  The title you want to assign to the SignatureRequest.  |  |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


