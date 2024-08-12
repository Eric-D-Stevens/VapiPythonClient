# Call

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of call. | [optional] 
**messages** | **list[OneOfCallMessagesItems]** | These are the messages that were spoken during the call. | [optional] 
**phone_call_provider** | **str** | This is the provider of the call.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**phone_call_transport** | **str** | This is the transport of the phone call.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**status** | **str** | This is the status of the call. | [optional] 
**ended_reason** | **str** | This is the explanation for how the call ended. | [optional] 
**destination** | **OneOfCallDestination** | This is the destination where the call ended up being transferred to. If the call was not transferred, this will be empty. | [optional] 
**id** | **str** | This is the unique identifier for the call. | 
**org_id** | **str** | This is the unique identifier for the org that this call belongs to. | 
**created_at** | **datetime** | This is the ISO 8601 date-time string of when the call was created. | 
**updated_at** | **datetime** | This is the ISO 8601 date-time string of when the call was last updated. | 
**started_at** | **datetime** | This is the ISO 8601 date-time string of when the call was started. | [optional] 
**ended_at** | **datetime** | This is the ISO 8601 date-time string of when the call was ended. | [optional] 
**cost** | **float** | This is the cost of the call in USD. | [optional] 
**cost_breakdown** | **AllOfCallCostBreakdown** | This is the cost of the call in USD. | [optional] 
**costs** | **list[object]** | These are the costs of individual components of the call in USD. | [optional] 
**transcript** | **str** | This is the transcript of the call. | [optional] 
**recording_url** | **str** | This is the URL of the recording of the call. | [optional] 
**stereo_recording_url** | **str** | This is the URL of the recording of the call in two channels. | [optional] 
**artifact** | **AllOfCallArtifact** | This stores artifacts of the call. Customize what artifacts are created by configuring &#x60;assistant.artifactPlan&#x60;. | [optional] 
**artifact_plan** | **AllOfCallArtifactPlan** | This is a copy of assistant artifact plan. This isn&#x27;t actually stored on the call but rather just returned in POST /call/web to enable artifact creation client side. | [optional] 
**analysis** | **AllOfCallAnalysis** | This is the analysis of the call. Customize the analysis by configuring &#x60;assistant.analysisPlan&#x60;. | [optional] 
**phone_call_provider_id** | **str** | The ID of the call as provided by the phone number service. callSid in Twilio. conversationUuid in Vonage.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**assistant_id** | **str** | This is the assistant that will be used for the call. To use a transient assistant, use &#x60;assistant&#x60; instead. | [optional] 
**assistant** | **AllOfCallAssistant** | This is the assistant that will be used for the call. To use an existing assistant, use &#x60;assistantId&#x60; instead. | [optional] 
**assistant_overrides** | **AllOfCallAssistantOverrides** | These are the overrides for the &#x60;assistant&#x60; or &#x60;assistantId&#x60;&#x27;s settings and template variables. | [optional] 
**squad_id** | **str** | This is the squad that will be used for the call. To use a transient squad, use &#x60;squad&#x60; instead. | [optional] 
**squad** | **AllOfCallSquad** | This is a squad that will be used for the call. To use an existing squad, use &#x60;squadId&#x60; instead. | [optional] 
**phone_number_id** | **str** | This is the phone number that will be used for the call. To use a transient number, use &#x60;phoneNumber&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**phone_number** | **AllOfCallPhoneNumber** | This is the phone number that will be used for the call. To use an existing number, use &#x60;phoneNumberId&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**customer_id** | **str** | This is the customer that will be called. To call a transient customer , use &#x60;customer&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**customer** | **AllOfCallCustomer** | This is the customer that will be called. To call an existing customer, use &#x60;customerId&#x60; instead.  Only relevant for &#x60;outboundPhoneCall&#x60; and &#x60;inboundPhoneCall&#x60; type. | [optional] 
**name** | **str** | This is the name of the call. This is just for your own reference. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

