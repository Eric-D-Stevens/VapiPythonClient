# DeepgramTranscriber

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | This is the transcription provider that will be used. | 
**model** | **OneOfDeepgramTranscriberModel** | This is the Deepgram model that will be used. A list of models can be found here: https://developers.deepgram.com/docs/models-languages-overview | [optional] 
**language** | **str** | This is the language that will be set for the transcription. The list of languages Deepgram supports can be found here: https://developers.deepgram.com/docs/models-languages-overview | [optional] 
**smart_format** | **bool** | This will be use smart format option provided by Deepgram. It&#x27;s default disabled because it can sometimes format numbers as times sometimes but it&#x27;s getting better. | [optional] 
**keywords** | **list[str]** | These keywords are passed to the transcription model to help it pick up use-case specific words. Anything that may not be a common word, like your company name, should be added here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

