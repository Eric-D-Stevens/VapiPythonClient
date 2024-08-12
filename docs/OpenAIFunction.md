# OpenAIFunction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the the name of the function to be called.  Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64. | 
**description** | **str** |  | [optional] 
**parameters** | **AllOfOpenAIFunctionParameters** | These are the parameters the functions accepts, described as a JSON Schema object.  See the [OpenAI guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format.  Omitting parameters defines a function with an empty parameter list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

