# ToolMessageStart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This message is triggered when the tool call starts.  This message is never triggered for async tools.  If this message is not provided, one of the default filler messages \&quot;Hold on a sec\&quot;, \&quot;One moment\&quot;, \&quot;Just a sec\&quot;, \&quot;Give me a moment\&quot; or \&quot;This&#x27;ll just take a sec\&quot; will be used. | 
**content** | **str** | This is the content that the assistant says when this message is triggered. | 
**conditions** | [**list[Condition]**](Condition.md) | This is an optional array of conditions that the tool call arguments must meet in order for this message to be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

