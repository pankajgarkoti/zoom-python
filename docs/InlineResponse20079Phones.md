# InlineResponse20079Phones

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_name** | **str** | The authorization name of the user that is registered for SIP phone. | [optional] 
**domain** | **str** | The name or IP address of your provider&#x27;s SIP domain. | [optional] 
**id** | **str** | The SIP phone ID. | [optional] 
**password** | **str** | The password generated for the user in the SIP account.  | [optional] 
**proxy_server** | **str** | The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty. | [optional] 
**proxy_server2** | **str** | The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty. | [optional] 
**proxy_server3** | **str** | The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty. | [optional] 
**register_server** | **str** | The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. | [optional] 
**register_server2** | **str** | The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. | [optional] 
**register_server3** | **str** | The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. | [optional] 
**registration_expire_time** | **int** | The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.  | [optional] 
**transport_protocol** | **str** | Protocols supported by the SIP provider.     The value must be either &#x60;UDP&#x60;, &#x60;TCP&#x60;, &#x60;TLS&#x60;, &#x60;AUTO&#x60;. | [optional] 
**transport_protocol2** | **str** | Protocols supported by the SIP provider.     The value must be either &#x60;UDP&#x60;, &#x60;TCP&#x60;, &#x60;TLS&#x60;, &#x60;AUTO&#x60;. | [optional] 
**transport_protocol3** | **str** | Protocols supported by the SIP provider.     The value must be either &#x60;UDP&#x60;, &#x60;TCP&#x60;, &#x60;TLS&#x60;, &#x60;AUTO&#x60;. | [optional] 
**user_email** | **str** | The email address of the user to associate with the SIP Phone. Can add &#x60;.win&#x60;, &#x60;.mac&#x60;, &#x60;.android&#x60;, &#x60;.ipad&#x60;, &#x60;.iphone&#x60;, &#x60;.linux&#x60;, &#x60;.pc&#x60;, &#x60;.mobile&#x60;, &#x60;.pad&#x60; at the end of the email (for example, &#x60;user@example.com.mac&#x60;) to add accounts for different platforms for the same user. | [optional] 
**user_name** | **str** | The phone number associated with the user in the SIP account.  | [optional] 
**voice_mail** | **str** | The number to dial for checking voicemail. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

