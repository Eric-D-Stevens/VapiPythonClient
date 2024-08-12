# AnyscaleModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**list[OpenAIMessage]**](OpenAIMessage.md) | This is the starting state for the conversation. | [optional] 
**tools** | **list[OneOfAnyscaleModelToolsItems]** | These are the tools that the assistant can use during the call. To use existing tools, use &#x60;toolIds&#x60;.  Both &#x60;tools&#x60; and &#x60;toolIds&#x60; can be used together. | [optional] 
**tool_ids** | **list[str]** | These are the tools that the assistant can use during the call. To use transient tools, use &#x60;tools&#x60;.  Both &#x60;tools&#x60; and &#x60;toolIds&#x60; can be used together. | [optional] 
**provider** | **str** |  | 
**model** | **str** | This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b | 
**temperature** | **float** | This is the temperature that will be used for calls. Default is 0 to leverage caching for lower latency. | [optional] 
**knowledge_base** | **AllOfAnyscaleModelKnowledgeBase** | These are the options for the knowledge base. | [optional] 
**max_tokens** | **float** | This is the max number of tokens that the assistant will be allowed to generate in each turn of the conversation. Default is 250. | [optional] 
**emotion_recognition_enabled** | **bool** | This determines whether we detect user&#x27;s emotion while they speak and send it as an additional info to model.  Default &#x60;false&#x60; because the model is usually are good at understanding the user&#x27;s emotion from text.  @default false | [optional] 
**num_fast_turns** | **float** | This sets how many turns at the start of the conversation to use a smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if provider is openai.  Default is 0.  @default 0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

