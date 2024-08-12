# CreateMakeToolDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_async** | **bool** | This determines if the tool is async.  If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.  If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.  Defaults to synchronous (&#x60;false&#x60;). | [optional] 
**messages** | **list[OneOfCreateMakeToolDTOMessagesItems]** | These are the messages that will be spoken to the user as the tool is running.  For some tools, this is auto-filled based on special fields like &#x60;tool.destinations&#x60;. For others like the function tool, these can be custom configured. | [optional] 
**type** | **str** | The type of tool. \&quot;make\&quot; for Make tool. | 
**metadata** | [**MakeToolMetadata**](MakeToolMetadata.md) |  | 
**function** | **AllOfCreateMakeToolDTOFunction** | This is the function definition of the tool.  For &#x60;endCall&#x60;, &#x60;transferCall&#x60;, and &#x60;dtmf&#x60; tools, this is auto-filled based on tool-specific fields like &#x60;tool.destinations&#x60;. But, even in those cases, you can provide a custom function definition for advanced use cases.  An example of an advanced use case is if you want to customize the message that&#x27;s spoken for &#x60;endCall&#x60; tool. You can specify a function where it returns an argument \&quot;reason\&quot;. Then, in &#x60;messages&#x60; array, you can have many \&quot;request-complete\&quot; messages. One of these messages will be triggered if the &#x60;messages[].conditions&#x60; matches the \&quot;reason\&quot; argument. | [optional] 
**server** | **AllOfCreateMakeToolDTOServer** | This is the server that will be hit when this tool is requested by the model.  All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.  This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

