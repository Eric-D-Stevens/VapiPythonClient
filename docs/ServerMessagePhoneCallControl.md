# ServerMessagePhoneCallControl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of the message. \&quot;phone-call-control\&quot; is an advanced type of message.  When it is requested in &#x60;assistant.serverMessages&#x60;, the hangup and forwarding responsibilities are delegated to your server. Vapi will no longer do the actual transfer and hangup. | 
**request** | **str** | This is the request to control the phone call. | 
**destination** | **OneOfServerMessagePhoneCallControlDestination** | This is the destination to forward the call to if the request is \&quot;forward\&quot;. | [optional] 
**phone_number** | **object** | The phone number associated with the call. This either directly matches &#x60;call.phoneNumber&#x60; or is expanded from &#x60;call.phoneNumberId&#x60;. | [optional] 
**customer** | **object** | The customer associated with the call. This either directly matches &#x60;call.customer&#x60; or is expanded from &#x60;call.customerId&#x60;. | 
**call** | **object** | This is the main &#x60;call&#x60; object of the call. | 
**artifact** | **object** | These are the live artifacts of the call. | [optional] 
**timestamp** | **str** | This is the timestamp of the message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

