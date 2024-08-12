# coding: utf-8

"""
    Vapi API

    API for building voice assistants  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vapi_python_client.api_client import ApiClient


class BlocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def block_controller_create(self, body, **kwargs):  # noqa: E501
        """Create Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BlockBody body: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.block_controller_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.block_controller_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def block_controller_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BlockBody body: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method block_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `block_controller_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/block', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def block_controller_find_all(self, **kwargs):  # noqa: E501
        """List Blocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_find_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float limit: This is the maximum number of items to return. Defaults to 100.
        :param datetime created_at_gt: This will return items where the createdAt is greater than the specified value.
        :param datetime created_at_lt: This will return items where the createdAt is less than the specified value.
        :param datetime created_at_ge: This will return items where the createdAt is greater than or equal to the specified value.
        :param datetime created_at_le: This will return items where the createdAt is less than or equal to the specified value.
        :param datetime updated_at_gt: This will return items where the updatedAt is greater than the specified value.
        :param datetime updated_at_lt: This will return items where the updatedAt is less than the specified value.
        :param datetime updated_at_ge: This will return items where the updatedAt is greater than or equal to the specified value.
        :param datetime updated_at_le: This will return items where the updatedAt is less than or equal to the specified value.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.block_controller_find_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.block_controller_find_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def block_controller_find_all_with_http_info(self, **kwargs):  # noqa: E501
        """List Blocks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_find_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float limit: This is the maximum number of items to return. Defaults to 100.
        :param datetime created_at_gt: This will return items where the createdAt is greater than the specified value.
        :param datetime created_at_lt: This will return items where the createdAt is less than the specified value.
        :param datetime created_at_ge: This will return items where the createdAt is greater than or equal to the specified value.
        :param datetime created_at_le: This will return items where the createdAt is less than or equal to the specified value.
        :param datetime updated_at_gt: This will return items where the updatedAt is greater than the specified value.
        :param datetime updated_at_lt: This will return items where the updatedAt is less than the specified value.
        :param datetime updated_at_ge: This will return items where the updatedAt is greater than or equal to the specified value.
        :param datetime updated_at_le: This will return items where the updatedAt is less than or equal to the specified value.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'created_at_gt', 'created_at_lt', 'created_at_ge', 'created_at_le', 'updated_at_gt', 'updated_at_lt', 'updated_at_ge', 'updated_at_le']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method block_controller_find_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'created_at_gt' in params:
            query_params.append(('createdAtGt', params['created_at_gt']))  # noqa: E501
        if 'created_at_lt' in params:
            query_params.append(('createdAtLt', params['created_at_lt']))  # noqa: E501
        if 'created_at_ge' in params:
            query_params.append(('createdAtGe', params['created_at_ge']))  # noqa: E501
        if 'created_at_le' in params:
            query_params.append(('createdAtLe', params['created_at_le']))  # noqa: E501
        if 'updated_at_gt' in params:
            query_params.append(('updatedAtGt', params['updated_at_gt']))  # noqa: E501
        if 'updated_at_lt' in params:
            query_params.append(('updatedAtLt', params['updated_at_lt']))  # noqa: E501
        if 'updated_at_ge' in params:
            query_params.append(('updatedAtGe', params['updated_at_ge']))  # noqa: E501
        if 'updated_at_le' in params:
            query_params.append(('updatedAtLe', params['updated_at_le']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/block', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def block_controller_find_one(self, id, **kwargs):  # noqa: E501
        """Get Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_find_one(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.block_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.block_controller_find_one_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def block_controller_find_one_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_find_one_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method block_controller_find_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `block_controller_find_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/block/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def block_controller_remove(self, id, **kwargs):  # noqa: E501
        """Delete Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_remove(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.block_controller_remove_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.block_controller_remove_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def block_controller_remove_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_remove_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method block_controller_remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `block_controller_remove`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/block/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def block_controller_update(self, body, id, **kwargs):  # noqa: E501
        """Update Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_update(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateBlockDTO body: (required)
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.block_controller_update_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.block_controller_update_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def block_controller_update_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update Block  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.block_controller_update_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateBlockDTO body: (required)
        :param str id: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method block_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `block_controller_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `block_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/block/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2011',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
