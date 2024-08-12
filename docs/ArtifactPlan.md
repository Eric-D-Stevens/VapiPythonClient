# ArtifactPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_recording_enabled** | **bool** | This determines whether the video is recorded during the call. Default is false. Only relevant for &#x60;webCall&#x60; type. | [optional] 
**recording_s3_path_prefix** | **str** | This is the S3 path prefix for the audio recording. This is only used if you have provided S3 credentials. Check the Providers page in the Dashboard.  If credential.s3PathPrefix is set, this will append to it.  Example: &#x60;/my-prefix&#x60;. Default is &#x60;/&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

