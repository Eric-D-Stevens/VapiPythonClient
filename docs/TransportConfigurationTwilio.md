# TransportConfigurationTwilio

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**timeout** | **float** | The integer number of seconds that we should allow the phone to ring before assuming there is no answer. The default is &#x60;60&#x60; seconds and the maximum is &#x60;600&#x60; seconds. For some call flows, we will add a 5-second buffer to the timeout value you provide. For this reason, a timeout value of 10 seconds could result in an actual timeout closer to 15 seconds. You can set this to a short time, such as &#x60;15&#x60; seconds, to hang up before reaching an answering machine or voicemail.  @default 60 | [optional] 
**record** | **bool** | Whether to record the call. Can be &#x60;true&#x60; to record the phone call, or &#x60;false&#x60; to not. The default is &#x60;false&#x60;.  @default false | [optional] 
**recording_channels** | **str** | The number of channels in the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60;. The default is &#x60;mono&#x60;. &#x60;mono&#x60; records both legs of the call in a single channel of the recording file. &#x60;dual&#x60; records each leg to a separate channel of the recording file. The first channel of a dual-channel recording contains the parent call and the second channel contains the child call.  @default &#x27;mono&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

