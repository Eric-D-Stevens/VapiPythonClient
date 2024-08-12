# TransferDestinationSip

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**sip_uri** | **str** | This is the SIP URI to transfer the call to. | 
**message** | **str** | This is the message to say before transferring the call to the destination.  If this is not provided and transfer tool messages is not provided, default is \&quot;Transferring the call now\&quot;.  If set to \&quot;\&quot;, nothing is spoken. This is useful when you want to silently transfer. This is especially useful when transferring between assistants in a squad. In this scenario, you likely also want to set &#x60;assistant.firstMessageMode&#x3D;assistant-speaks-first-with-model-generated-message&#x60; for the destination assistant. | [optional] 
**description** | **str** | This is the description of the destination, used by the AI to choose when and how to transfer the call. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

