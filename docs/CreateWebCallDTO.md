# CreateWebCallDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant_id** | **str** | This is the assistant that will be used for the call. To use a transient assistant, use &#x60;assistant&#x60; instead. | [optional] 
**assistant** | **AllOfCreateWebCallDTOAssistant** | This is the assistant that will be used for the call. To use an existing assistant, use &#x60;assistantId&#x60; instead. | [optional] 
**assistant_overrides** | **AllOfCreateWebCallDTOAssistantOverrides** | These are the overrides for the &#x60;assistant&#x60; or &#x60;assistantId&#x60;&#x27;s settings and template variables. | [optional] 
**squad_id** | **str** | This is the squad that will be used for the call. To use a transient squad, use &#x60;squad&#x60; instead. | [optional] 
**squad** | **AllOfCreateWebCallDTOSquad** | This is a squad that will be used for the call. To use an existing squad, use &#x60;squadId&#x60; instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

