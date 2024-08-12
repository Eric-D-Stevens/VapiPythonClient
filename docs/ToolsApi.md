# vapi_python_client.ToolsApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_controller_create**](ToolsApi.md#tool_controller_create) | **POST** /tool | Create Tool
[**tool_controller_find_all**](ToolsApi.md#tool_controller_find_all) | **GET** /tool | List Tools
[**tool_controller_find_one**](ToolsApi.md#tool_controller_find_one) | **GET** /tool/{id} | Get Tool
[**tool_controller_remove**](ToolsApi.md#tool_controller_remove) | **DELETE** /tool/{id} | Delete Tool
[**tool_controller_update**](ToolsApi.md#tool_controller_update) | **PATCH** /tool/{id} | Update Tool

# **tool_controller_create**
> InlineResponse2012 tool_controller_create(body)

Create Tool

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.ToolsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.ToolBody() # ToolBody | 

try:
    # Create Tool
    api_response = api_instance.tool_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->tool_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ToolBody**](ToolBody.md)|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_controller_find_all**
> list[object] tool_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)

List Tools

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.ToolsApi(vapi_python_client.ApiClient(configuration))
limit = 1.2 # float | This is the maximum number of items to return. Defaults to 100. (optional)
created_at_gt = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the createdAt is greater than the specified value. (optional)
created_at_lt = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the createdAt is less than the specified value. (optional)
created_at_ge = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the createdAt is greater than or equal to the specified value. (optional)
created_at_le = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the createdAt is less than or equal to the specified value. (optional)
updated_at_gt = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the updatedAt is greater than the specified value. (optional)
updated_at_lt = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the updatedAt is less than the specified value. (optional)
updated_at_ge = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the updatedAt is greater than or equal to the specified value. (optional)
updated_at_le = '2013-10-20T19:20:30+01:00' # datetime | This will return items where the updatedAt is less than or equal to the specified value. (optional)

try:
    # List Tools
    api_response = api_instance.tool_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->tool_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| This is the maximum number of items to return. Defaults to 100. | [optional] 
 **created_at_gt** | **datetime**| This will return items where the createdAt is greater than the specified value. | [optional] 
 **created_at_lt** | **datetime**| This will return items where the createdAt is less than the specified value. | [optional] 
 **created_at_ge** | **datetime**| This will return items where the createdAt is greater than or equal to the specified value. | [optional] 
 **created_at_le** | **datetime**| This will return items where the createdAt is less than or equal to the specified value. | [optional] 
 **updated_at_gt** | **datetime**| This will return items where the updatedAt is greater than the specified value. | [optional] 
 **updated_at_lt** | **datetime**| This will return items where the updatedAt is less than the specified value. | [optional] 
 **updated_at_ge** | **datetime**| This will return items where the updatedAt is greater than or equal to the specified value. | [optional] 
 **updated_at_le** | **datetime**| This will return items where the updatedAt is less than or equal to the specified value. | [optional] 

### Return type

**list[object]**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_controller_find_one**
> InlineResponse2012 tool_controller_find_one(id)

Get Tool

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.ToolsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Tool
    api_response = api_instance.tool_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->tool_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_controller_remove**
> InlineResponse2012 tool_controller_remove(id)

Delete Tool

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.ToolsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Tool
    api_response = api_instance.tool_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->tool_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tool_controller_update**
> InlineResponse2012 tool_controller_update(body, id)

Update Tool

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.ToolsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdateToolDTO() # UpdateToolDTO | 
id = 'id_example' # str | 

try:
    # Update Tool
    api_response = api_instance.tool_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolsApi->tool_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateToolDTO**](UpdateToolDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

