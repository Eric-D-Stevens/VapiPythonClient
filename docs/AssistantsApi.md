# vapi_python_client.AssistantsApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assistant_controller_create**](AssistantsApi.md#assistant_controller_create) | **POST** /assistant | Create Assistant
[**assistant_controller_find_all**](AssistantsApi.md#assistant_controller_find_all) | **GET** /assistant | List Assistants
[**assistant_controller_find_one**](AssistantsApi.md#assistant_controller_find_one) | **GET** /assistant/{id} | Get Assistant
[**assistant_controller_remove**](AssistantsApi.md#assistant_controller_remove) | **DELETE** /assistant/{id} | Delete Assistant
[**assistant_controller_update**](AssistantsApi.md#assistant_controller_update) | **PATCH** /assistant/{id} | Update Assistant

# **assistant_controller_create**
> Assistant assistant_controller_create(body)

Create Assistant

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AssistantsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.CreateAssistantDTO() # CreateAssistantDTO | 

try:
    # Create Assistant
    api_response = api_instance.assistant_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantsApi->assistant_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAssistantDTO**](CreateAssistantDTO.md)|  | 

### Return type

[**Assistant**](Assistant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assistant_controller_find_all**
> list[Assistant] assistant_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)

List Assistants

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AssistantsApi(vapi_python_client.ApiClient(configuration))
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
    # List Assistants
    api_response = api_instance.assistant_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantsApi->assistant_controller_find_all: %s\n" % e)
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

[**list[Assistant]**](Assistant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assistant_controller_find_one**
> Assistant assistant_controller_find_one(id)

Get Assistant

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AssistantsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Assistant
    api_response = api_instance.assistant_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantsApi->assistant_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assistant_controller_remove**
> Assistant assistant_controller_remove(id)

Delete Assistant

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AssistantsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Assistant
    api_response = api_instance.assistant_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantsApi->assistant_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assistant_controller_update**
> Assistant assistant_controller_update(body, id)

Update Assistant

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.AssistantsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdateAssistantDTO() # UpdateAssistantDTO | 
id = 'id_example' # str | 

try:
    # Update Assistant
    api_response = api_instance.assistant_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantsApi->assistant_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAssistantDTO**](UpdateAssistantDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**Assistant**](Assistant.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

