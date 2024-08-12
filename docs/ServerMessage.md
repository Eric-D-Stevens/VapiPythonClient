# ServerMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **OneOfServerMessageMessage** | These are all the messages that can be sent to your server before, after and during the call. Configure the messages you&#x27;d like to receive in &#x60;assistant.serverMessages&#x60;.  The server where the message is sent is determined by the following precedence order:  1. &#x60;tool.server.url&#x60; (if configured, and only for \&quot;tool-calls\&quot; message) 2. &#x60;assistant.serverUrl&#x60; (if configure) 3. &#x60;phoneNumber.serverUrl&#x60; (if configured) 4. &#x60;org.serverUrl&#x60; (if configured) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

