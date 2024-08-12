# vapi_python_client.CallsApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_controller_create**](CallsApi.md#call_controller_create) | **POST** /call | Create Call
[**call_controller_delete_call_data**](CallsApi.md#call_controller_delete_call_data) | **DELETE** /call/{id} | Delete Call Data
[**call_controller_find_all**](CallsApi.md#call_controller_find_all) | **GET** /call | List Calls
[**call_controller_find_one**](CallsApi.md#call_controller_find_one) | **GET** /call/{id} | Get Call
[**call_controller_update**](CallsApi.md#call_controller_update) | **PATCH** /call/{id} | Update Call

# **call_controller_create**
> Call call_controller_create(body)

Create Call

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.CallsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.CreateCallDTO() # CreateCallDTO | 

try:
    # Create Call
    api_response = api_instance.call_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCallDTO**](CreateCallDTO.md)|  | 

### Return type

[**Call**](Call.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_controller_delete_call_data**
> Call call_controller_delete_call_data(id)

Delete Call Data

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.CallsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Call Data
    api_response = api_instance.call_controller_delete_call_data(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_controller_delete_call_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Call**](Call.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_controller_find_all**
> list[Call] call_controller_find_all(assistant_id=assistant_id, limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)

List Calls

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.CallsApi(vapi_python_client.ApiClient(configuration))
assistant_id = 'assistant_id_example' # str | This will return calls with the specified assistantId. (optional)
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
    # List Calls
    api_response = api_instance.call_controller_find_all(assistant_id=assistant_id, limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_controller_find_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | **str**| This will return calls with the specified assistantId. | [optional] 
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

[**list[Call]**](Call.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_controller_find_one**
> Call call_controller_find_one(id)

Get Call

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.CallsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Call
    api_response = api_instance.call_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Call**](Call.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_controller_update**
> Call call_controller_update(body, id)

Update Call

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.CallsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdateCallDTO() # UpdateCallDTO | 
id = 'id_example' # str | 

try:
    # Update Call
    api_response = api_instance.call_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->call_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCallDTO**](UpdateCallDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**Call**](Call.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

