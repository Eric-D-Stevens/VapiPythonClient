# UpdateBlockDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **list[OneOfUpdateBlockDTOMessagesItems]** | These are the pre-configured messages that will be spoken to the user while the block is running. | [optional] 
**input_schema** | **AllOfUpdateBlockDTOInputSchema** | This is the input schema for the block. This is the input the block needs to run. It&#x27;s given to the block as &#x60;steps[0].input&#x60;  These are accessible as variables: - ({{input.propertyName}}) in context of the block execution (step) - ({{stepName.input.propertyName}}) in context of the workflow | [optional] 
**output_schema** | **AllOfUpdateBlockDTOOutputSchema** | This is the output schema for the block. This is the output the block will return to the workflow (&#x60;{{stepName.output}}&#x60;).  These are accessible as variables: - ({{output.propertyName}}) in context of the block execution (step) - ({{stepName.output.propertyName}}) in context of the workflow | [optional] 
**tool** | **OneOfUpdateBlockDTOTool** | This is the tool that the block will call. To use an existing tool, use &#x60;toolId&#x60;. | [optional] 
**steps** | **list[OneOfUpdateBlockDTOStepsItems]** | These are the steps in the workflow. | [optional] 
**name** | **str** | This is the name of the block. This is just for your reference. | [optional] 
**instruction** | **str** | This is the instruction to the model.  You can reference any variable in the context of the current block execution (step): - \&quot;{{input.your-property-name}}\&quot; for the current step&#x27;s input - \&quot;{{your-step-name.output.your-property-name}}\&quot; for another step&#x27;s output (in the same workflow) - \&quot;{{your-step-name.input.your-property-name}}\&quot; for another step&#x27;s input (in the same workflow) - \&quot;{{workflow.input.your-property-name}}\&quot; for the current workflow&#x27;s input - \&quot;{{global.your-property-name}}\&quot; for the global context  This can be as simple or as complex as you want it to be. - \&quot;say hello and ask the user about their day!\&quot; - \&quot;collect the user&#x27;s first and last name\&quot; - \&quot;user is {{input.firstName}} {{input.lastName}}. their age is {{input.age}}. ask them about their salary and if they might be interested in buying a house. we offer {{input.offer}}\&quot; | [optional] 
**tool_id** | **str** | This is the id of the tool that the block will call. To use a transient tool, use &#x60;tool&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

