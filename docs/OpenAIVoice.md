# OpenAIVoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_preprocessing_enabled** | **bool** | This determines whether the model output is preprocessed into chunks before being sent to the voice provider.  Default &#x60;true&#x60; because voice generation sounds better with chunking (and reformatting them).  To send every token from the model output directly to the voice provider and rely on the voice provider&#x27;s audio generation logic, set this to &#x60;false&#x60;.  If disabled, vapi-provided audio control tokens like &lt;flush /&gt; will not work. | [optional] 
**input_reformatting_enabled** | **bool** | This determines whether the chunk is reformatted before being sent to the voice provider. Many things are reformatted including phone numbers, emails and addresses to improve their enunciation.  Default &#x60;true&#x60; because voice generation sounds better with reformatting.  To disable chunk reformatting, set this to &#x60;false&#x60;.  To disable chunking completely, set &#x60;inputPreprocessingEnabled&#x60; to &#x60;false&#x60;. | [optional] 
**input_min_characters** | **float** | This is the minimum number of characters before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults to 30.  Increasing this value might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, increasing might be a good idea if you want to give voice provider bigger chunks so it can pronounce them better.  Decreasing this value might decrease latency but might also decrease quality if the voice provider struggles to pronounce the text correctly. | [optional] 
**input_punctuation_boundaries** | **list[str]** | These are the punctuations that are considered valid boundaries before a chunk is created. The chunks that are sent to the voice provider for the voice generation as the model tokens are streaming in. Defaults are chosen differently for each provider.  Constraining the delimiters might add latency as it waits for the model to output a full chunk before sending it to the voice provider. On the other hand, constraining might be a good idea if you want to give voice provider longer chunks so it can sound less disjointed across chunks. Eg. [&#x27;.&#x27;]. | [optional] 
**filler_injection_enabled** | **bool** | This determines whether fillers are injected into the model output before inputting it into the voice provider.  Default &#x60;false&#x60; because you can achieve better results with prompting the model. | [optional] 
**provider** | **str** | This is the voice provider that will be used. | 
**voice_id** | **OneOfOpenAIVoiceVoiceId** | This is the provider-specific ID that will be used. | 
**speed** | **float** | This is the speed multiplier that will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

