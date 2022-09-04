# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Finds the @endpoint decorator parameter values"""

import ast

from chess_pieces.rests.base_viewset.endpoint_metadata import EndpointMetadata


class EndpointDecoratorVisitor(ast.NodeVisitor):
    """Finds the @endpoint decorator parameter values"""

    def __init__(self):
        super(EndpointDecoratorVisitor, self).__init__()
        self._endpoints = list()

    def generic_visit(self, node):
        """
        :param _ast.Module node:
        """
        if isinstance(node, ast.FunctionDef):
            endpoint_decorator = EndpointDecoratorVisitor._get_endpoint_decorator(node)

            if endpoint_decorator:
                method_name = node.name
                path = EndpointDecoratorVisitor._get_endpoint_path(endpoint_decorator)
                http_method = EndpointDecoratorVisitor._get_endpoint_http_method(endpoint_decorator)
                endpoint_metadata = EndpointMetadata(method_name, path, http_method)
                self._endpoints.append(endpoint_metadata)

        # Recursion
        super(EndpointDecoratorVisitor, self).generic_visit(node)

    @property
    def endpoints(self):
        """
        :return list[EndpointMetadata]:
        """
        return self._endpoints

    @staticmethod
    def _get_endpoint_decorator(node):
        """
        :param ast.FunctionDef node:
        :return ast.Call:
        """
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Call):
                if decorator.func.__dict__.get('attr') == 'endpoint':
                    return decorator

    @staticmethod
    def _get_endpoint_path(decorator):
        """
        :param ast.Call decorator:
        :return str:
        """
        parameter_path = [k for k in decorator.keywords if k.arg.lower() == 'path']

        if parameter_path:
            return parameter_path[0].value.value

    @staticmethod
    def _get_endpoint_http_method(decorator):
        """
        :param ast.Call decorator:
        :return str:
        """
        parameter_http_method = [k for k in decorator.keywords if k.arg.lower() == 'http_method']

        if parameter_http_method:
            return parameter_http_method[0].value.value
