# ToolMessageComplete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This message is triggered when the tool call is complete.  This message is triggered immediately without waiting for your server to respond for async tool calls.  If this message is not provided, the model will be requested to respond.  If this message is provided, only this message will be spoken and the model will not be requested to come up with a response. It&#x27;s an exclusive OR. | 
**role** | **str** | This is optional and defaults to \&quot;assistant\&quot;.  When role&#x3D;assistant, &#x60;content&#x60; is said out loud.  When role&#x3D;system, &#x60;content&#x60; is passed to the model in a system message. Example:     system: default one     assistant:     user:     assistant:     user:     assistant:     user:     assistant: tool called     tool: your server response     &lt;--- system prompt as hint     ---&gt; model generates response which is spoken This is useful when you want to provide a hint to the model about what to say next. | [optional] 
**end_call_after_spoken_enabled** | **bool** | This is an optional boolean that if true, the call will end after the message is spoken. Default is false.  This is ignored if &#x60;role&#x60; is set to &#x60;system&#x60;.  @default false | [optional] 
**content** | **str** | This is the content that the assistant says when this message is triggered. | 
**conditions** | [**list[Condition]**](Condition.md) | This is an optional array of conditions that the tool call arguments must meet in order for this message to be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

