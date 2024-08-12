# VapiPhoneNumber

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_destination** | **OneOfVapiPhoneNumberFallbackDestination** | This is the fallback destination an inbound call will be transferred to if: 1. &#x60;assistantId&#x60; is not set 2. &#x60;squadId&#x60; is not set 3. and, &#x60;assistant-request&#x60; message to the &#x60;serverUrl&#x60; fails  If this is not set and above conditions are met, the inbound call is hung up with an error message. | [optional] 
**provider** | **str** | This is to create free SIP phone numbers on Vapi. | 
**id** | **str** | This is the unique identifier for the phone number. | 
**org_id** | **str** | This is the unique identifier for the org that this phone number belongs to. | 
**created_at** | **datetime** | This is the ISO 8601 date-time string of when the phone number was created. | 
**updated_at** | **datetime** | This is the ISO 8601 date-time string of when the phone number was last updated. | 
**name** | **str** | This is the name of the phone number. This is just for your own reference. | [optional] 
**assistant_id** | **str** | This is the assistant that will be used for incoming calls to this phone number.  If neither &#x60;assistantId&#x60; nor &#x60;squadId&#x60; is set, &#x60;assistant-request&#x60; will be sent to your Server URL. Check &#x60;ServerMessage&#x60; and &#x60;ServerMessageResponse&#x60; for the shape of the message and response that is expected. | [optional] 
**squad_id** | **str** | This is the squad that will be used for incoming calls to this phone number.  If neither &#x60;assistantId&#x60; nor &#x60;squadId&#x60; is set, &#x60;assistant-request&#x60; will be sent to your Server URL. Check &#x60;ServerMessage&#x60; and &#x60;ServerMessageResponse&#x60; for the shape of the message and response that is expected. | [optional] 
**server_url** | **str** | This is the server URL where messages will be sent for calls on this number. This includes the &#x60;assistant-request&#x60; message.  You can see the shape of the messages sent in &#x60;ServerMessage&#x60;.  This overrides the &#x60;org.serverUrl&#x60;. Order of precedence: tool.server.url &gt; assistant.serverUrl &gt; phoneNumber.serverUrl &gt; org.serverUrl. | [optional] 
**server_url_secret** | **str** | This is the secret Vapi will send with every message to your server. It&#x27;s sent as a header called x-vapi-secret.  Same precedence logic as serverUrl. | [optional] 
**sip_uri** | **str** | This is the SIP URI of the phone number. You can SIP INVITE this. The assistant attached to this number will answer. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

