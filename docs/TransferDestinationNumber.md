# TransferDestinationNumber

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**number_e164_check_enabled** | **bool** | This is the flag to toggle the E164 check for the &#x60;number&#x60; field. This is an advanced property which should be used if you know your use case requires it.  Use cases: - &#x60;false&#x60;: To allow non-E164 numbers like &#x60;+001234567890&#x60;, &#x60;1234&#x27;, or &#x60;abc&#x60;. This is useful for dialing out to non-E164 numbers on your SIP trunks. - &#x60;true&#x60; (default): To allow only E164 numbers like &#x60;+14155551234&#x60;. This is for most standard PSTN calls.  If &#x60;false&#x60;, the &#x60;number&#x60; is still required to only contain alphanumeric characters (regex: &#x60;/^\\+?[a-zA-Z0-9]+$/&#x60;).  @default true (E164 check is enabled) | [optional] [default to True]
**number** | **str** | This is the phone number to transfer the call to. | 
**extension** | **str** | This is the extension to dial after transferring the call to the &#x60;number&#x60;. | [optional] 
**message** | **str** | This is the message to say before transferring the call to the destination.  If this is not provided and transfer tool messages is not provided, default is \&quot;Transferring the call now\&quot;.  If set to \&quot;\&quot;, nothing is spoken. This is useful when you want to silently transfer. This is especially useful when transferring between assistants in a squad. In this scenario, you likely also want to set &#x60;assistant.firstMessageMode&#x3D;assistant-speaks-first-with-model-generated-message&#x60; for the destination assistant. | [optional] 
**description** | **str** | This is the description of the destination, used by the AI to choose when and how to transfer the call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

