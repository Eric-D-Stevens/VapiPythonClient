# ServerMessageAssistantRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of the message. \&quot;assistant-request\&quot; is sent to fetch assistant configuration for an incoming call. | 
**phone_number** | **object** | The phone number associated with the call. This either directly matches &#x60;call.phoneNumber&#x60; or is expanded from &#x60;call.phoneNumberId&#x60;. | [optional] 
**customer** | **object** | The customer associated with the call. This either directly matches &#x60;call.customer&#x60; or is expanded from &#x60;call.customerId&#x60;. | 
**call** | **object** | This is the main &#x60;call&#x60; object of the call. | 
**artifact** | **object** | These are the live artifacts of the call. | [optional] 
**timestamp** | **str** | This is the timestamp of the message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

