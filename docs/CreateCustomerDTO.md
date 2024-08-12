# CreateCustomerDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_e164_check_enabled** | **bool** | This is the flag to toggle the E164 check for the &#x60;number&#x60; field. This is an advanced property which should be used if you know your use case requires it.  Use cases: - &#x60;false&#x60;: To allow non-E164 numbers like &#x60;+001234567890&#x60;, &#x60;1234&#x27;, or &#x60;abc&#x60;. This is useful for dialing out to non-E164 numbers on your SIP trunks. - &#x60;true&#x60; (default): To allow only E164 numbers like &#x60;+14155551234&#x60;. This is for most standard PSTN calls.  If &#x60;false&#x60;, the &#x60;number&#x60; is still required to only contain alphanumeric characters (regex: &#x60;/^\\+?[a-zA-Z0-9]+$/&#x60;).  @default true (E164 check is enabled) | [optional] [default to True]
**extension** | **str** | This is the extension that will be dialed after the call is answered. | [optional] 
**number** | **str** | This is the number of the customer. | [optional] 
**sip_uri** | **str** | This is the SIP URI of the customer. | [optional] 
**name** | **str** | This is the name of the customer. This is just for your own reference. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

