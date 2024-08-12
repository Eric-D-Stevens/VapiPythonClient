# CreateByoPhoneNumberDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback_destination** | **OneOfCreateByoPhoneNumberDTOFallbackDestination** | This is the fallback destination an inbound call will be transferred to if: 1. &#x60;assistantId&#x60; is not set 2. &#x60;squadId&#x60; is not set 3. and, &#x60;assistant-request&#x60; message to the &#x60;serverUrl&#x60; fails  If this is not set and above conditions are met, the inbound call is hung up with an error message. | [optional] 
**provider** | **str** | This is to bring your own phone numbers from your own SIP trunks or Carriers. | 
**number** | **str** | These are the digits of the phone number you own on your SIP trunk or Carrier.  This is not limited to E164 and can be any alphanumeric string. Example: &#x60;+1234567890&#x60;, or &#x60;abc&#x60;, or &#x60;1234&#x27;. | 
**credential_id** | **str** | This is the credential of your own SIP trunk or Carrier (type &#x60;byo-sip-trunk&#x60;) which can be used to make calls to this phone number.  You can add the SIP trunk or Carrier credential in the Provider Credentials page on the Dashboard to get the credentialId. | 
**name** | **str** | This is the name of the phone number. This is just for your own reference. | [optional] 
**assistant_id** | **str** | This is the assistant that will be used for incoming calls to this phone number.  If neither &#x60;assistantId&#x60; nor &#x60;squadId&#x60; is set, &#x60;assistant-request&#x60; will be sent to your Server URL. Check &#x60;ServerMessage&#x60; and &#x60;ServerMessageResponse&#x60; for the shape of the message and response that is expected. | [optional] 
**squad_id** | **str** | This is the squad that will be used for incoming calls to this phone number.  If neither &#x60;assistantId&#x60; nor &#x60;squadId&#x60; is set, &#x60;assistant-request&#x60; will be sent to your Server URL. Check &#x60;ServerMessage&#x60; and &#x60;ServerMessageResponse&#x60; for the shape of the message and response that is expected. | [optional] 
**server_url** | **str** | This is the server URL where messages will be sent for calls on this number. This includes the &#x60;assistant-request&#x60; message.  You can see the shape of the messages sent in &#x60;ServerMessage&#x60;.  This overrides the &#x60;org.serverUrl&#x60;. Order of precedence: tool.server.url &gt; assistant.serverUrl &gt; phoneNumber.serverUrl &gt; org.serverUrl. | [optional] 
**server_url_secret** | **str** | This is the secret Vapi will send with every message to your server. It&#x27;s sent as a header called x-vapi-secret.  Same precedence logic as serverUrl. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

