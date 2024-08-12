# TokenRestrictions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | This determines whether the token is enabled or disabled. Default is true, it&#x27;s enabled. | [optional] 
**allowed_origins** | **list[str]** | This determines the allowed origins for this token. Validates the &#x60;Origin&#x60; header. Default is any origin.  Only relevant for &#x60;public&#x60; tokens. | [optional] 
**allowed_assistant_ids** | **list[str]** | This determines which assistantIds can be used when creating a call. Default is any assistantId.  Only relevant for &#x60;public&#x60; tokens. | [optional] 
**allow_transient_assistant** | **bool** | This determines whether transient assistants can be used when creating a call. Default is true.  If &#x60;allowedAssistantIds&#x60; is provided, this is automatically false.  Only relevant for &#x60;public&#x60; tokens. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

