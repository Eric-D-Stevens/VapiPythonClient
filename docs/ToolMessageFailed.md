# ToolMessageFailed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This message is triggered when the tool call fails.  This message is never triggered for async tool calls.  If this message is not provided, the model will be requested to respond.  If this message is provided, only this message will be spoken and the model will not be requested to come up with a response. It&#x27;s an exclusive OR. | 
**end_call_after_spoken_enabled** | **bool** | This is an optional boolean that if true, the call will end after the message is spoken. Default is false.  @default false | [optional] 
**content** | **str** | This is the content that the assistant says when this message is triggered. | 
**conditions** | [**list[Condition]**](Condition.md) | This is an optional array of conditions that the tool call arguments must meet in order for this message to be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

