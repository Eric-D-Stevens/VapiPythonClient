# CreateByoSipTrunkCredentialDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | This can be used to bring your own SIP trunks or to connect to a Carrier. | [optional] 
**gateways** | [**list[SipTrunkGateway]**](SipTrunkGateway.md) | This is the list of SIP trunk&#x27;s gateways. | 
**name** | **str** | This is the name of the SIP trunk. This is just for your reference. | [optional] 
**outbound_authentication_plan** | **AllOfCreateByoSipTrunkCredentialDTOOutboundAuthenticationPlan** | This can be used to configure the outbound authentication if required by the SIP trunk. | [optional] 
**sbc_configuration** | **AllOfCreateByoSipTrunkCredentialDTOSbcConfiguration** | This is an advanced configuration for enterprise deployments. This uses the onprem SBC to trunk into the SIP trunk&#x27;s &#x60;gateways&#x60;, rather than the managed SBC provided by Vapi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

