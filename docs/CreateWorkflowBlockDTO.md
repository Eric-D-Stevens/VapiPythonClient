# CreateWorkflowBlockDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **list[OneOfCreateWorkflowBlockDTOMessagesItems]** | These are the pre-configured messages that will be spoken to the user while the block is running. | [optional] 
**input_schema** | **AllOfCreateWorkflowBlockDTOInputSchema** | This is the input schema for the block. This is the input the block needs to run. It&#x27;s given to the block as &#x60;steps[0].input&#x60;  These are accessible as variables: - ({{input.propertyName}}) in context of the block execution (step) - ({{stepName.input.propertyName}}) in context of the workflow | [optional] 
**output_schema** | **AllOfCreateWorkflowBlockDTOOutputSchema** | This is the output schema for the block. This is the output the block will return to the workflow (&#x60;{{stepName.output}}&#x60;).  These are accessible as variables: - ({{output.propertyName}}) in context of the block execution (step) - ({{stepName.output.propertyName}}) in context of the workflow | [optional] 
**type** | **str** | This creates a workflow which can contain any number of steps (block executions). | 
**steps** | **list[OneOfCreateWorkflowBlockDTOStepsItems]** | These are the steps in the workflow. | [optional] 
**name** | **str** | This is the name of the block. This is just for your reference. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

