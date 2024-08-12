# JsonSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This is the type of output you&#x27;d like.  &#x60;string&#x60;, &#x60;number&#x60;, &#x60;integer&#x60;, &#x60;boolean&#x60; are the primitive types and should be obvious.  &#x60;array&#x60; and &#x60;object&#x60; are more interesting and quite powerful. They allow you to define nested structures.  For &#x60;array&#x60;, you can define the schema of the items in the array using the &#x60;items&#x60; property.  For &#x60;object&#x60;, you can define the properties of the object using the &#x60;properties&#x60; property. | 
**items** | **object** | This is required if the type is \&quot;array\&quot;. This is the schema of the items in the array.  This is of type JsonSchema. However, Swagger doesn&#x27;t support circular references. | [optional] 
**properties** | **object** | This is required if the type is \&quot;object\&quot;. This specifies the properties of the object.  This is a map of string to JsonSchema. However, Swagger doesn&#x27;t support circular references. | [optional] 
**description** | **str** | This is the description to help the model understand what it needs to output. | [optional] 
**required** | **list[str]** | This is a list of properties that are required.  This only makes sense if the type is \&quot;object\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

