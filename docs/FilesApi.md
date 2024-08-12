# vapi_python_client.FilesApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_controller_create**](FilesApi.md#file_controller_create) | **POST** /file | Upload File
[**file_controller_find_all**](FilesApi.md#file_controller_find_all) | **GET** /file | List Files
[**file_controller_find_one**](FilesApi.md#file_controller_find_one) | **GET** /file/{id} | Get File
[**file_controller_remove**](FilesApi.md#file_controller_remove) | **DELETE** /file/{id} | Delete File
[**file_controller_update**](FilesApi.md#file_controller_update) | **PATCH** /file/{id} | Update File

# **file_controller_create**
> File file_controller_create(file)

Upload File

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.FilesApi(vapi_python_client.ApiClient(configuration))
file = 'file_example' # str | 

try:
    # Upload File
    api_response = api_instance.file_controller_create(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->file_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_controller_find_all**
> list[File] file_controller_find_all()

List Files

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.FilesApi(vapi_python_client.ApiClient(configuration))

try:
    # List Files
    api_response = api_instance.file_controller_find_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->file_controller_find_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[File]**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_controller_find_one**
> File file_controller_find_one(id)

Get File

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.FilesApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get File
    api_response = api_instance.file_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->file_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_controller_remove**
> File file_controller_remove(id)

Delete File

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.FilesApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete File
    api_response = api_instance.file_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->file_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_controller_update**
> File file_controller_update(body, id)

Update File

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.FilesApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdateFileDTO() # UpdateFileDTO | 
id = 'id_example' # str | 

try:
    # Update File
    api_response = api_instance.file_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->file_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateFileDTO**](UpdateFileDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**File**](File.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

