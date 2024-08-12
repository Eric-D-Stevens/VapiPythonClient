# ToolMessageDelayed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This message is triggered when the tool call is delayed.  There are the two things that can trigger this message: 1. The user talks with the assistant while your server is processing the request. Default is \&quot;Sorry, a few more seconds.\&quot; 2. The server doesn&#x27;t respond within &#x60;timingMilliseconds&#x60;.  This message is never triggered for async tool calls. | 
**timing_milliseconds** | **float** | The number of milliseconds to wait for the server response before saying this message. | [optional] 
**content** | **str** | This is the content that the assistant says when this message is triggered. | 
**conditions** | [**list[Condition]**](Condition.md) | This is an optional array of conditions that the tool call arguments must meet in order for this message to be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

