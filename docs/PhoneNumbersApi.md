# vapi_python_client.PhoneNumbersApi

All URIs are relative to *https://api.vapi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phone_number_controller_create**](PhoneNumbersApi.md#phone_number_controller_create) | **POST** /phone-number | Create Phone Number
[**phone_number_controller_find_all**](PhoneNumbersApi.md#phone_number_controller_find_all) | **GET** /phone-number | List Phone Numbers
[**phone_number_controller_find_one**](PhoneNumbersApi.md#phone_number_controller_find_one) | **GET** /phone-number/{id} | Get Phone Number
[**phone_number_controller_remove**](PhoneNumbersApi.md#phone_number_controller_remove) | **DELETE** /phone-number/{id} | Delete Phone Number
[**phone_number_controller_update**](PhoneNumbersApi.md#phone_number_controller_update) | **PATCH** /phone-number/{id} | Update Phone Number

# **phone_number_controller_create**
> InlineResponse201 phone_number_controller_create(body)

Create Phone Number

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.PhoneNumbersApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.PhonenumberBody() # PhonenumberBody | 

try:
    # Create Phone Number
    api_response = api_instance.phone_number_controller_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->phone_number_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhonenumberBody**](PhonenumberBody.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_number_controller_find_all**
> list[object] phone_number_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)

List Phone Numbers

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.PhoneNumbersApi(vapi_python_client.ApiClient(configuration))
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
    # List Phone Numbers
    api_response = api_instance.phone_number_controller_find_all(limit=limit, created_at_gt=created_at_gt, created_at_lt=created_at_lt, created_at_ge=created_at_ge, created_at_le=created_at_le, updated_at_gt=updated_at_gt, updated_at_lt=updated_at_lt, updated_at_ge=updated_at_ge, updated_at_le=updated_at_le)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->phone_number_controller_find_all: %s\n" % e)
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

# **phone_number_controller_find_one**
> InlineResponse201 phone_number_controller_find_one(id)

Get Phone Number

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.PhoneNumbersApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Phone Number
    api_response = api_instance.phone_number_controller_find_one(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->phone_number_controller_find_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_number_controller_remove**
> InlineResponse201 phone_number_controller_remove(id)

Delete Phone Number

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.PhoneNumbersApi(vapi_python_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete Phone Number
    api_response = api_instance.phone_number_controller_remove(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->phone_number_controller_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phone_number_controller_update**
> InlineResponse201 phone_number_controller_update(body, id)

Update Phone Number

### Example
```python
from __future__ import print_function
import time
import vapi_python_client
from vapi_python_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = vapi_python_client.PhoneNumbersApi(vapi_python_client.ApiClient(configuration))
body = vapi_python_client.UpdatePhoneNumberDTO() # UpdatePhoneNumberDTO | 
id = 'id_example' # str | 

try:
    # Update Phone Number
    api_response = api_instance.phone_number_controller_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhoneNumbersApi->phone_number_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePhoneNumberDTO**](UpdatePhoneNumberDTO.md)|  | 
 **id** | **str**|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

