# MessagePlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_messages** | **list[str]** | This are the messages that the assistant will speak when the user hasn&#x27;t responded for &#x60;idleTimeoutSeconds&#x60;. Each time the timeout is triggered, a random message will be chosen from this array.  @default null (no idle message is spoken) | [optional] 
**idle_message_max_spoken_count** | **float** | This determines the maximum number of times &#x60;idleMessages&#x60; can be spoken during the call.  @default 3 | [optional] 
**idle_timeout_seconds** | **float** | This is the timeout in seconds before a message from &#x60;idleMessages&#x60; is spoken. The clock starts when the assistant finishes speaking and remains active until the user speaks.  @default 10 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

