# AnalyticsQueryResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the unique key for the query. | 
**time_range** | **AllOfAnalyticsQueryResultTimeRange** | This is the time range for the query. | 
**result** | **list[object]** | This is the result of the query, a list of unique groups with result of their aggregations.  Example: \&quot;result\&quot;: [   { \&quot;date\&quot;: \&quot;2023-01-01\&quot;, \&quot;assistantId\&quot;: \&quot;123\&quot;, \&quot;endedReason\&quot;: \&quot;customer-ended-call\&quot;, \&quot;sumDuration\&quot;: 120, \&quot;avgCost\&quot;: 10.5 },   { \&quot;date\&quot;: \&quot;2023-01-02\&quot;, \&quot;assistantId\&quot;: \&quot;123\&quot;, \&quot;endedReason\&quot;: \&quot;customer-did-not-give-microphone-permission\&quot;, \&quot;sumDuration\&quot;: 0, \&quot;avgCost\&quot;: 0 },   // Additional results ] | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

