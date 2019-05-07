# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CaptureApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config) 


    def capture_payment(self, capture_payment_request, id, **kwargs):
        """
        Capture a Payment
        Include the payment ID in the POST request to capture the payment amount.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.capture_payment(capture_payment_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CapturePaymentRequest capture_payment_request: (required)
        :param str id: The payment ID returned from a previous payment request. This ID links the capture to the payment.  (required)
        :return: PtsV2PaymentsCapturesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.capture_payment_with_http_info(capture_payment_request, id, **kwargs)
        else:
            (data) = self.capture_payment_with_http_info(capture_payment_request, id, **kwargs)
            return data

    def capture_payment_with_http_info(self, capture_payment_request, id, **kwargs):
        """
        Capture a Payment
        Include the payment ID in the POST request to capture the payment amount.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.capture_payment_with_http_info(capture_payment_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CapturePaymentRequest capture_payment_request: (required)
        :param str id: The payment ID returned from a previous payment request. This ID links the capture to the payment.  (required)
        :return: PtsV2PaymentsCapturesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['capture_payment_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method capture_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'capture_payment_request' is set
        if ('capture_payment_request' not in params) or (params['capture_payment_request'] is None):
            raise ValueError("Missing the required parameter `capture_payment_request` when calling `capture_payment`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `capture_payment`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'capture_payment_request' in params:
            body_params = params['capture_payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v2/payments/' + id + '/captures', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2PaymentsCapturesPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
