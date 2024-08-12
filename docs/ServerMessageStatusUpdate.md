# ServerMessageStatusUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of the message. \&quot;status-update\&quot; is sent whenever the &#x60;call.status&#x60; changes. | 
**status** | **str** | This is the status of the call. | 
**ended_reason** | **str** | This is the reason the call ended. This is only sent if the status is \&quot;ended\&quot;. | [optional] 
**messages** | **list[OneOfServerMessageStatusUpdateMessagesItems]** | These are the conversation messages of the call. This is only sent if the status is \&quot;forwarding\&quot;. | [optional] 
**messages_open_ai_formatted** | [**list[OpenAIMessage]**](OpenAIMessage.md) | These are the conversation messages of the call. This is only sent if the status is \&quot;forwarding\&quot;. | [optional] 
**destination** | **OneOfServerMessageStatusUpdateDestination** | This is the destination the call is being transferred to. This is only sent if the status is \&quot;forwarding\&quot;. | [optional] 
**phone_number** | **object** | The phone number associated with the call. This either directly matches &#x60;call.phoneNumber&#x60; or is expanded from &#x60;call.phoneNumberId&#x60;. | [optional] 
**customer** | **object** | The customer associated with the call. This either directly matches &#x60;call.customer&#x60; or is expanded from &#x60;call.customerId&#x60;. | 
**call** | **object** | This is the main &#x60;call&#x60; object of the call. | 
**artifact** | **object** | These are the live artifacts of the call. | [optional] 
**timestamp** | **str** | This is the timestamp of the message. | [optional] 
**transcript** | **str** | This is the transcript of the call. This is only sent if the status is \&quot;forwarding\&quot;. | [optional] 
**inbound_phone_call_debugging_artifacts** | **object** | This is the inbound phone call debugging artifacts. This is only sent if the status is \&quot;ended\&quot; and there was an error accepting the inbound phone call.  This will include any errors related to the \&quot;assistant-request\&quot; if one was made. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

