# OpenAIFunctionParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This must be set to &#x27;object&#x27;. It instructs the model to return a JSON object containing the function call properties. | 
**properties** | [**dict(str, JsonSchema)**](JsonSchema.md) | This provides a description of the properties required by the function. JSON Schema can be used to specify expectations for each property. Refer to [this doc](https://ajv.js.org/json-schema.html#json-data-type) for a comprehensive guide on JSON Schema. | 
**required** | **list[str]** | This specifies the properties that are required by the function. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

