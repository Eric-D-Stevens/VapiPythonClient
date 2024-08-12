# ModelBasedCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This condition is based on a model. | 
**instruction** | **str** | This is the instruction which should output a boolean value when passed to a model.  You can reference any variable in the context of the current block execution (step): - \&quot;{{output.your-property-name}}\&quot; for current step&#x27;s output - \&quot;{{input.your-property-name}}\&quot; for current step&#x27;s input - \&quot;{{your-step-name.output.your-property-name}}\&quot; for another step&#x27;s output (in the same workflow) - \&quot;{{your-step-name.input.your-property-name}}\&quot; for another step&#x27;s input (in the same workflow) - \&quot;{{workflow.input.your-property-name}}\&quot; for the current workflow&#x27;s input - \&quot;{{global.your-property-name}}\&quot; for the global context  You can also talk about the current step&#x27;s output or input directly: - \&quot;{{output.your-property-name}} is greater than 10\&quot; - \&quot;{{input.your-property-name}} is greater than 10\&quot;  Examples:  - \&quot;{{input.age}} is greater than 10\&quot;  - \&quot;{{input.age}} is greater than {{input.age2}}\&quot;  - \&quot;{{output.age}} is greater than 10\&quot; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

