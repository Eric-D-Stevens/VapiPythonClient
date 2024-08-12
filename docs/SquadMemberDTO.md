# SquadMemberDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistant_id** | **str** | This is the assistant that will be used for the call. To use a transient assistant, use &#x60;assistant&#x60; instead. | [optional] 
**assistant** | **AllOfSquadMemberDTOAssistant** | This is the assistant that will be used for the call. To use an existing assistant, use &#x60;assistantId&#x60; instead. | [optional] 
**assistant_overrides** | **AllOfSquadMemberDTOAssistantOverrides** | This can be used to override the assistant&#x27;s settings and provide values for it&#x27;s template variables. | [optional] 
**assistant_destinations** | [**list[TransferDestinationAssistant]**](TransferDestinationAssistant.md) | These are the others assistants that this assistant can transfer to.  If the assistant already has transfer call tool, these destinations are just appended to existing ones. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

