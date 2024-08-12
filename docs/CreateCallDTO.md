# CreateCallDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the call. This is just for your own reference. | [optional] 
**assistant_id** | **str** | This is the assistant that will be used for the call. To use a transient assistant, use &#x60;assistant&#x60; instead. | [optional] 
**assistant** | **AllOfCreateCallDTOAssistant** | This is the assistant that will be used for the call. To use an existing assistant, use &#x60;assistantId&#x60; instead. | [optional] 
**assistant_overrides** | **AllOfCreateCallDTOAssistantOverrides** | These are the overrides for the &#x60;assistant&#x60; or &#x60;assistantId&#x60;&#x27;s settings and template variables. | [optional] 
**squad_id** | **str** | This is the squad that will be used for the call. To use a transient squad, use &#x60;squad&#x60; instead. | [optional] 
**squad** | **AllOfCreateCallDTOSquad** | This is a squad that will be used for the call. To use an existing squad, use &#x60;squadId&#x60; instead. | [optional] 
**phone_number_id** | **str** | This is the phone number that will be used for the call. To use a transient number, use &#x60;phoneNumber&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**phone_number** | **AllOfCreateCallDTOPhoneNumber** | This is the phone number that will be used for the call. To use an existing number, use &#x60;phoneNumberId&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**customer_id** | **str** | This is the customer that will be called. To call a transient customer , use &#x60;customer&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**customer** | **AllOfCreateCallDTOCustomer** | This is the customer that will be called. To call an existing customer, use &#x60;customerId&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

