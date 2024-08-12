# GladiaTranscriber

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | This is the transcription provider that will be used. | 
**model** | **OneOfGladiaTranscriberModel** | This is the Gladia model that will be used. Default is &#x27;fast&#x27; | [optional] 
**language_behaviour** | **OneOfGladiaTranscriberLanguageBehaviour** | Defines how the transcription model detects the audio language. Default value is &#x27;automatic single language&#x27;. | [optional] 
**language** | **str** | Defines the language to use for the transcription. Required when languageBehaviour is &#x27;manual&#x27;. | [optional] 
**transcription_hint** | **str** | Provides a custom vocabulary to the model to improve accuracy of transcribing context specific words, technical terms, names, etc. If empty, this argument is ignored. ⚠️ Warning ⚠️: Please be aware that the transcription_hint field has a character limit of 600. If you provide a transcription_hint longer than 600 characters, it will be automatically truncated to meet this limit. | [optional] 
**prosody** | **bool** | If prosody is true, you will get a transcription that can contain prosodies i.e. (laugh) (giggles) (malefic laugh) (toss) (music)… Default value is false. | [optional] 
**audio_enhancer** | **bool** | If true, audio will be pre-processed to improve accuracy but latency will increase. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

