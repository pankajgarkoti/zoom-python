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


class ContactGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def contact_group(self, group_id, **kwargs):  # noqa: E501
        """Get a contact group  # noqa: E501

        Get a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def contact_group_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Get a contact group  # noqa: E501

        Get a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `contact_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

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
            '/contacts/groups/{groupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contact_group_create(self, **kwargs):  # noqa: E501
        """Create a contact group  # noqa: E501

        Use this API to create a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactsGroupsBody body:
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def contact_group_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a contact group  # noqa: E501

        Use this API to create a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactsGroupsBody body:
        :return: InlineResponse2012
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
                    " to method contact_group_create" % key
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
            '/contacts/groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2012',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contact_group_delete(self, group_id, **kwargs):  # noqa: E501
        """Delete a contact group  # noqa: E501

        Use this API to delete a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_delete(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_delete_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_delete_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def contact_group_delete_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Delete a contact group  # noqa: E501

        Use this API to delete a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_delete_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `contact_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/groups/{groupId}', 'DELETE',
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

    def contact_group_member_add(self, **kwargs):  # noqa: E501
        """Add contact group members  # noqa: E501

        Use this API to add members to a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_member_add(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupIdMembersBody body:
        :return: InlineResponse2013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_member_add_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_member_add_with_http_info(**kwargs)  # noqa: E501
            return data

    def contact_group_member_add_with_http_info(self, **kwargs):  # noqa: E501
        """Add contact group members  # noqa: E501

        Use this API to add members to a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_member_add_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GroupIdMembersBody body:
        :return: InlineResponse2013
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
                    " to method contact_group_member_add" % key
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
            '/contacts/groups/{groupId}/members', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contact_group_member_remove(self, member_ids, **kwargs):  # noqa: E501
        """Remove members in a contact group  # noqa: E501

        Use this API to remove members in a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_member_remove(member_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_ids: The member's ID in a contact group. Use commas (,) to separate a maximum of 20 ids.      Can be retrieved by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroupMembers) API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_member_remove_with_http_info(member_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_member_remove_with_http_info(member_ids, **kwargs)  # noqa: E501
            return data

    def contact_group_member_remove_with_http_info(self, member_ids, **kwargs):  # noqa: E501
        """Remove members in a contact group  # noqa: E501

        Use this API to remove members in a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-).  **Prerequisite**: Pro or higher account.      **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_member_remove_with_http_info(member_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str member_ids: The member's ID in a contact group. Use commas (,) to separate a maximum of 20 ids.      Can be retrieved by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroupMembers) API. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['member_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_group_member_remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'member_ids' is set
        if ('member_ids' not in params or
                params['member_ids'] is None):
            raise ValueError("Missing the required parameter `member_ids` when calling `contact_group_member_remove`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'member_ids' in params:
            query_params.append(('member_ids', params['member_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['openapi_authorization', 'openapi_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/groups/{groupId}/members', 'DELETE',
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

    def contact_group_members(self, **kwargs):  # noqa: E501
        """List contact group members  # noqa: E501

        List members in [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_members(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_members_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_members_with_http_info(**kwargs)  # noqa: E501
            return data

    def contact_group_members_with_http_info(self, **kwargs):  # noqa: E501
        """List contact group members  # noqa: E501

        List members in [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_members_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_group_members" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page_token' in params:
            query_params.append(('next_page_token', params['next_page_token']))  # noqa: E501

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
            '/contacts/groups/{groupId}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20015',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contact_group_update(self, group_id, **kwargs):  # noqa: E501
        """Update a contact group  # noqa: E501

        Update a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_update(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :param GroupsGroupIdBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_group_update_with_http_info(group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.contact_group_update_with_http_info(group_id, **kwargs)  # noqa: E501
            return data

    def contact_group_update_with_http_info(self, group_id, **kwargs):  # noqa: E501
        """Update a contact group  # noqa: E501

        Update a [contact group](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under your account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:write:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_group_update_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_id: The contact group ID.     Retrieve by calling the [**List contact groups**](/docs/api-reference/zoom-api/methods#operation/contactGroups) API. (required)
        :param GroupsGroupIdBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_group_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params or
                params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `contact_group_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['groupId'] = params['group_id']  # noqa: E501

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
            '/contacts/groups/{groupId}', 'PATCH',
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

    def contact_groups(self, **kwargs):  # noqa: E501
        """List contact groups  # noqa: E501

        List [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_groups(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.contact_groups_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.contact_groups_with_http_info(**kwargs)  # noqa: E501
            return data

    def contact_groups_with_http_info(self, **kwargs):  # noqa: E501
        """List contact groups  # noqa: E501

        List [contact groups](https://support.zoom.us/hc/en-us/articles/204519819-Group-Management-) under an account.  **Prerequisite**: Pro or higher account.       **Scopes:** `contact_group:read:admin`  **[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contact_groups_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: The number of records returned with a single API call. 
        :param str next_page_token: The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'next_page_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contact_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page_token' in params:
            query_params.append(('next_page_token', params['next_page_token']))  # noqa: E501

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
            '/contacts/groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20013',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
