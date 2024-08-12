# ClientMessageToolCalls

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of the message. \&quot;tool-calls\&quot; is sent to call a tool. | [optional] 
**tool_with_tool_call_list** | **list[OneOfClientMessageToolCallsToolWithToolCallListItems]** | This is the list of tools calls that the model is requesting along with the original tool configuration. | 
**tool_call_list** | [**list[ToolCall]**](ToolCall.md) | This is the list of tool calls that the model is requesting. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

