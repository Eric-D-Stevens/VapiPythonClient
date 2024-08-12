# vapi_python_client.AnalyticsApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_controller_query**](AnalyticsApi.md#analytics_controller_query) | **POST** /analytics | Create Analytics Queries

# **analytics_controller_query**
> list[AnalyticsQueryResult] analytics_controller_query(body)

Create Analytics Queries

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AnalyticsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.AnalyticsQueryDTO() # AnalyticsQueryDTO | 

try:
    # Create Analytics Queries
    api_response = api_instance.analytics_controller_query(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_controller_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsQueryDTO**](AnalyticsQueryDTO.md)|  | 

### Return type

[**list[AnalyticsQueryResult]**](AnalyticsQueryResult.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

