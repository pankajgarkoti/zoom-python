# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zoom.api_client import ApiClient


class TrackingFieldApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def trackingfield_create(self, **kwargs):  # noqa: E501
        """Create a tracking field  # noqa: E501

        Use this API to create a new [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). Tracking fields let you analyze usage by various fields within an organization. When scheduling a meeting, tracking fields will be included in the meeting options.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField body: Tracking Field
        :return: TrackingField1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def trackingfield_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a tracking field  # noqa: E501

        Use this API to create a new [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). Tracking fields let you analyze usage by various fields within an organization. When scheduling a meeting, tracking fields will be included in the meeting options.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TrackingField body: Tracking Field
        :return: TrackingField1
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
                    " to method trackingfield_create" % key
                )
            params[key] = val
        del params['kwargs']

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
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrackingField1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_delete(self, field_id, **kwargs):  # noqa: E501
        """Delete a tracking field  # noqa: E501

        Use this API to delete a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_delete(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_delete_with_http_info(field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_delete_with_http_info(field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_delete_with_http_info(self, field_id, **kwargs):  # noqa: E501
        """Delete a tracking field  # noqa: E501

        Use this API to delete a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_delete_with_http_info(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_get(self, field_id, **kwargs):  # noqa: E501
        """Get a tracking field  # noqa: E501

        Use this API to return information about a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_get(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: TrackingField1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_get_with_http_info(field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_get_with_http_info(field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_get_with_http_info(self, field_id, **kwargs):  # noqa: E501
        """Get a tracking field  # noqa: E501

        Use this API to return information about a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_get_with_http_info(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :return: TrackingField1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrackingField1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_list(self, **kwargs):  # noqa: E501
        """List tracking fields  # noqa: E501

        Use this API to list all the [tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) on your Zoom account. Tracking fields let you analyze usage by various fields within an organization.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20082
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def trackingfield_list_with_http_info(self, **kwargs):  # noqa: E501
        """List tracking fields  # noqa: E501

        Use this API to list all the [tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) on your Zoom account. Tracking fields let you analyze usage by various fields within an organization.   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20082
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20082',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trackingfield_update(self, field_id, **kwargs):  # noqa: E501
        """Update a tracking field  # noqa: E501

        Use this API to update a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :param TrackingField2 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trackingfield_update_with_http_info(field_id, **kwargs)  # noqa: E501
        else:
            (data) = self.trackingfield_update_with_http_info(field_id, **kwargs)  # noqa: E501
            return data

    def trackingfield_update_with_http_info(self, field_id, **kwargs):  # noqa: E501
        """Update a tracking field  # noqa: E501

        Use this API to update a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields).   **Prerequisites:**  * A Business, Education, API or higher plan.  **Scopes:** `tracking_fields:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trackingfield_update_with_http_info(field_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str field_id: The Tracking Field ID (required)
        :param TrackingField2 body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['field_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trackingfield_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'field_id' is set
        if ('field_id' not in params or
                params['field_id'] is None):
            raise ValueError("Missing the required parameter `field_id` when calling `trackingfield_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'field_id' in params:
            path_params['fieldId'] = params['field_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/tracking_fields/{fieldId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
