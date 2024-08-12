# UpdateOrgDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hipaa_enabled** | **bool** | When this is enabled, no logs, recordings, or transcriptions will be stored. At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults to false. When HIPAA is enabled, only OpenAI/Custom LLM or Azure Providers will be available for LLM and Voice respectively. This is due to the compliance requirements of HIPAA. Other providers may not meet these requirements. | [optional] 
**name** | **str** | This is the name of the org. This is just for your own reference. | [optional] 
**billing_limit** | **float** | This is the monthly billing limit for the org. To go beyond $1000/mo, please contact us at support@vapi.ai. | [optional] 
**server_url** | **str** | This is the URL Vapi will communicate with via HTTP GET and POST Requests. This is used for retrieving context, function calling, and end-of-call reports.  All requests will be sent with the call object among other things relevant to that message. You can find more details in the Server URL documentation. | [optional] 
**server_url_secret** | **str** | This is the secret you can set that Vapi will send with every request to your server. Will be sent as a header called x-vapi-secret. | [optional] 
**concurrency_limit** | **float** | This is the concurrency limit for the org. This is the maximum number of calls that can be active at any given time. To go beyond 10, please contact us at support@vapi.ai. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

