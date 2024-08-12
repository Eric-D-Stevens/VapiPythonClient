# ServerMessageEndOfCallReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of the message. \&quot;end-of-call-report\&quot; is sent when the call ends and post-processing is complete. | 
**ended_reason** | **str** | This is the reason the call ended. | 
**messages** | **list[OneOfServerMessageEndOfCallReportMessagesItems]** | These are the message history of the call. The format is not OpenAI format but a custom VAPI format. | [optional] 
**recording_url** | **str** | This is the URL of the call recording. | [optional] 
**stereo_recording_url** | **str** | This is the URL of the stereo call recording. | [optional] 
**recording_wav** | **object** | This is the WAV buffer of the call recording. | [optional] 
**phone_number** | **object** | The phone number associated with the call. This either directly matches &#x60;call.phoneNumber&#x60; or is expanded from &#x60;call.phoneNumberId&#x60;. | [optional] 
**customer** | **object** | The customer associated with the call. This either directly matches &#x60;call.customer&#x60; or is expanded from &#x60;call.customerId&#x60;. | 
**call** | **object** | This is the main &#x60;call&#x60; object of the call. | 
**artifact** | **AllOfServerMessageEndOfCallReportArtifact** | These are the artifacts from the call. | [optional] 
**timestamp** | **str** | This is the timestamp of the message. | [optional] 
**transcript** | **str** | This is the transcript of the call. | 
**summary** | **str** | This is the summary of the call. | 
**analysis** | **AllOfServerMessageEndOfCallReportAnalysis** | This is the analysis of the call. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

