# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""It holds the metadata related to an endpoint"""


class EndpointMetadata:
    """It holds the metadata related to an endpoint"""

    def __init__(self, cls_method_name, endpoint_path, endpoint_http_method):
        """
        :param str cls_method_name:
        :param str endpoint_path:
        :param str endpoint_http_method:
        """
        self._cls_method_name = cls_method_name
        self._endpoint_path = endpoint_path
        self._endpoint_http_method = endpoint_http_method

    @property
    def cls_method_name(self):
        """
        :return str:
        """
        return self._cls_method_name

    @property
    def endpoint_path(self):
        """
        :return str:
        """
        return self._endpoint_path

    @property
    def endpoint_http_method(self):
        """
        :return str:
        """
        return self._endpoint_http_method
