# CreateS3CredentialDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Credential provider. Only allowed value is s3 | 
**aws_access_key_id** | **str** | AWS access key ID. | 
**aws_secret_access_key** | **str** | AWS access key secret. This is not returned in the API. | 
**region** | **str** | AWS region in which the S3 bucket is located. | 
**s3_bucket_name** | **str** | AWS S3 bucket name. | 
**s3_path_prefix** | **str** | The path prefix for the uploaded recording. Ex. \&quot;recordings/\&quot; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

