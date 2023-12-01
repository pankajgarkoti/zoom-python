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

from swagger_client.api_client import ApiClient


class InformationBarriersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def information_barriers_create(self, **kwargs):  # noqa: E501
        """Create an Information Barrier policy  # noqa: E501

        Create a new Information Barrier policy. [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) help customers control communication policies and meet regulatory requirements at scale. Use information barriers to prevent specific groups of users who possess sensitive information from communicating with others who should not know this information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InformationBarriersPoliciesBody body: Information Barriers object
        :return: InlineResponse2019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.information_barriers_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.information_barriers_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def information_barriers_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create an Information Barrier policy  # noqa: E501

        Create a new Information Barrier policy. [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) help customers control communication policies and meet regulatory requirements at scale. Use information barriers to prevent specific groups of users who possess sensitive information from communicating with others who should not know this information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param InformationBarriersPoliciesBody body: Information Barriers object
        :return: InlineResponse2019
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
                    " to method information_barriers_create" % key
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
            '/information_barriers/policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def information_barriers_delete(self, policy_id, **kwargs):  # noqa: E501
        """Remove an Information Barrier policy  # noqa: E501

        Remove an [Information Barrier](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_delete(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barriers policy's ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.information_barriers_delete_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.information_barriers_delete_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def information_barriers_delete_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Remove an Information Barrier policy  # noqa: E501

        Remove an [Information Barrier](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_delete_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barriers policy's ID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method information_barriers_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `information_barriers_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/information_barriers/policies/{policyId}', 'DELETE',
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

    def information_barriers_get(self, policy_id, **kwargs):  # noqa: E501
        """Get an Information Barrier policy by ID  # noqa: E501

        Return an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy by its ID.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_get(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barrier policy's ID. (required)
        :return: InlineResponse2019
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.information_barriers_get_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.information_barriers_get_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def information_barriers_get_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Get an Information Barrier policy by ID  # noqa: E501

        Return an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy by its ID.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_get_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barrier policy's ID. (required)
        :return: InlineResponse2019
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method information_barriers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `information_barriers_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/information_barriers/policies/{policyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2019',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def information_barriers_list(self, **kwargs):  # noqa: E501
        """List information Barrier policies  # noqa: E501

        Return a list of all [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policies and their information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20043
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.information_barriers_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.information_barriers_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def information_barriers_list_with_http_info(self, **kwargs):  # noqa: E501
        """List information Barrier policies  # noqa: E501

        Return a list of all [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policies and their information.    **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20043
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
                    " to method information_barriers_list" % key
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
            '/information_barriers/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20043',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def information_barriers_update(self, policy_id, **kwargs):  # noqa: E501
        """Update an Information Barriers policy  # noqa: E501

        Update an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_update(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barriers policy's ID. (required)
        :param PoliciesPolicyIdBody body: Information about the updated Information Barriers policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.information_barriers_update_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.information_barriers_update_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def information_barriers_update_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Update an Information Barriers policy  # noqa: E501

        Update an [Information Barriers](https://support.zoom.us/hc/en-us/articles/360040913711-Information-Barriers) policy.   **Prerequisites:**  * [Contact Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to enable Information Barriers for your account.  **Scopes:** `information_barriers:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.information_barriers_update_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: The Information Barriers policy's ID. (required)
        :param PoliciesPolicyIdBody body: Information about the updated Information Barriers policy.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method information_barriers_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `information_barriers_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/information_barriers/policies/{policyId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)