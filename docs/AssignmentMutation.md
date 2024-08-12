# AssignmentMutation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **list[OneOfAssignmentMutationConditionsItems]** | This is an optional array of conditions that must be met for this mutation to be triggered. | [optional] 
**type** | **str** | This mutation assigns a new value to an existing or new variable. | 
**variable** | **str** | This is the variable to assign a new value to.  You can reference any variable in the context of the current block execution (step): - \&quot;output.your-property-name\&quot; for current step&#x27;s output - \&quot;your-step-name.output.your-property-name\&quot; for another step&#x27;s output (in the same workflow) - \&quot;global.your-property-name\&quot; for the global context  This needs to be the key path of the variable. If you use {{}}, it&#x27;ll dereference that to the value of the variable before assignment. This can be useful if the path is dynamic. Example: - \&quot;global.{{my-tool-call-step.output.my-key-name}}\&quot;  You can also string interpolate multiple variables to get the key name: - \&quot;global.{{my-tool-call-step.output.my-key-name-suffix}}-{{my-tool-call-step.output.my-key-name}}\&quot;  The path to the new variable is created if it doesn&#x27;t exist. Example: - \&quot;global.this-does-not-exist.neither-does-this\&quot; will create &#x60;this-does-not-exist&#x60; object with &#x60;neither-does-this&#x60; as a key | 
**value** | **str** | The value to assign to the variable.  You can reference any variable in the context of the current block execution (step): - \&quot;{{output.your-property-name}}\&quot; for current step&#x27;s output - \&quot;{{your-step-name.output.your-property-name}}\&quot; for another step&#x27;s output (in the same workflow) - \&quot;{{global.your-property-name}}\&quot; for the global context  Or, you can use a constant: - \&quot;1\&quot; - \&quot;text\&quot; - \&quot;true\&quot; - \&quot;false\&quot;  Or, you can mix and match with string interpolation: - \&quot;{{your-property-name}}-{{input.your-property-name-2}}-1\&quot; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

