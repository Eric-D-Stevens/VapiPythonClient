# ServerMessageResponseAssistantRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **OneOfServerMessageResponseAssistantRequestDestination** | This is the destination to transfer the inbound call to. This will immediately transfer without using any assistants.  If this is sent, &#x60;assistantId&#x60;, &#x60;assistant&#x60;, &#x60;squadId&#x60;, and &#x60;squad&#x60; are ignored. | [optional] 
**assistant_id** | **str** | This is the assistant that will be used for the call. To use a transient assistant, use &#x60;assistant&#x60; instead. | [optional] 
**assistant** | **AllOfServerMessageResponseAssistantRequestAssistant** | This is the assistant that will be used for the call. To use an existing assistant, use &#x60;assistantId&#x60; instead.  If you&#x27;re unsure why you&#x27;re getting an invalid assistant, try logging your response and send the JSON blob to POST /assistant which will return the validation errors. | [optional] 
**assistant_overrides** | **AllOfServerMessageResponseAssistantRequestAssistantOverrides** | These are the overrides for the &#x60;assistant&#x60; or &#x60;assistantId&#x60;&#x27;s settings and template variables. | [optional] 
**squad_id** | **str** | This is the squad that will be used for the call. To use a transient squad, use &#x60;squad&#x60; instead. | [optional] 
**squad** | **AllOfServerMessageResponseAssistantRequestSquad** | This is a squad that will be used for the call. To use an existing squad, use &#x60;squadId&#x60; instead. | [optional] 
**error** | **str** | This is the error if the call shouldn&#x27;t be accepted. This is spoken to the customer.  If this is sent, &#x60;assistantId&#x60;, &#x60;assistant&#x60;, &#x60;squadId&#x60;, &#x60;squad&#x60;, and &#x60;destination&#x60; are ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

