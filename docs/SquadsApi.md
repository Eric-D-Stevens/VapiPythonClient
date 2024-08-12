# vapi_python_client.SquadsApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**squad_controller_create**](SquadsApi.md#squad_controller_create) | **POST** /squad | Create Squad
[**squad_controller_find_all**](SquadsApi.md#squad_controller_find_all) | **GET** /squad | List Squads
[**squad_controller_find_one**](SquadsApi.md#squad_controller_find_one) | **GET** /squad/{id} | Get Squad
[**squad_controller_remove**](SquadsApi.md#squad_controller_remove) | **DELETE** /squad/{id} | Delete Squad
[**squad_controller_update**](SquadsApi.md#squad_controller_update) | **PATCH** /squad/{id} | Update Squad

# **squad_controller_create**
> Squad squad_controller_create(body)

Create Squad

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.SquadsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.CreateSquadDTO() # CreateSquadDTO | 

try:
    # Create Squad
    api_response = api_instance.squad_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SquadsApi->squad_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSquadDTO**](CreateSquadDTO.md)|  | 

### Return type

[**Squad**](Squad.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **squad_controller_find_all**
> list[Squad] squad_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)

List Squads

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.SquadsApi(vapi_python_client.ApiClient(configuration))
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
    # List Squads
    api_response = api_instance.squad_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SquadsApi->squad_controller_find_all: %s\n" % e)
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

[**list[Squad]**](Squad.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **squad_controller_find_one**
> Squad squad_controller_find_one(id)

Get Squad

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.SquadsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Squad
    api_response = api_instance.squad_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SquadsApi->squad_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Squad**](Squad.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **squad_controller_remove**
> Squad squad_controller_remove(id)

Delete Squad

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.SquadsApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Squad
    api_response = api_instance.squad_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SquadsApi->squad_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Squad**](Squad.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **squad_controller_update**
> Squad squad_controller_update(body, id)

Update Squad

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.SquadsApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdateSquadDTO() # UpdateSquadDTO | 
id = 'id_example' # str | 

try:
    # Update Squad
    api_response = api_instance.squad_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SquadsApi->squad_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSquadDTO**](UpdateSquadDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**Squad**](Squad.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

