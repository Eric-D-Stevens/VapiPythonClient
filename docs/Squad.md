# Squad

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of the squad. | [optional] 
**members** | [**list[SquadMemberDTO]**](SquadMemberDTO.md) | This is the list of assistants that make up the squad.  The call will start with the first assistant in the list. | 
**members_overrides** | **AllOfSquadMembersOverrides** | This can be used to override all the assistants&#x27; settings and provide values for their template variables.  Both &#x60;membersOverrides&#x60; and &#x60;members[n].assistantOverrides&#x60; can be used together. First, &#x60;members[n].assistantOverrides&#x60; is applied. Then, &#x60;membersOverrides&#x60; is applied as a global override. | [optional] 
**id** | **str** | This is the unique identifier for the squad. | 
**org_id** | **str** | This is the unique identifier for the org that this squad belongs to. | 
**created_at** | **datetime** | This is the ISO 8601 date-time string of when the squad was created. | 
**updated_at** | **datetime** | This is the ISO 8601 date-time string of when the squad was last updated. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

