import ast
import inspect
from abc import ABC

from django.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ViewSet

from chess_pieces.rests.base_viewset.endpoint_decorator_visitor import EndpointDecoratorVisitor
from chess_pieces.rests.base_viewset.json_renderer import JSONRenderer


class GenericViewSet(ViewSet, ABC):
    """Generic ViewSet"""

    renderer_classes = [JSONRenderer]
    url_prefix = None
    url_basename = None
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @classmethod
    def build_urls(cls):
        """
        :return django.urls.path:
        :raise: TypeError
        """
        cls._assert_prefix()
        cls._assert_basename()
        default_actions_urls = cls._build_default_actions_urls()
        endpoint_actions_urls = cls._build_endpoint_actions_urls()
        return path('', include(default_actions_urls + endpoint_actions_urls))

    @classmethod
    def _get_endpoints(cls):
        """
        :return list[base.viewset.endpoint_metadata.EndpointMetadata]:
        """
        src = inspect.getsource(cls)
        tree = ast.parse(src)
        visitor = EndpointDecoratorVisitor()
        visitor.generic_visit(tree)
        return visitor.endpoints

    @classmethod
    def _build_default_actions_urls(cls):
        """
        :return list[django.urls.URLPattern]:
        """
        router = SimpleRouter()
        router.register(cls.url_prefix, cls, basename=cls.url_basename)
        return router.urls

    @classmethod
    def _build_endpoint_actions_urls(cls):
        """
        :return list[django.urls.URLPattern]:
        """
        endpoints = cls._get_endpoints()
        paths = list()

        for endpoint in endpoints:
            view = cls.as_view({endpoint.endpoint_http_method: endpoint.cls_method_name})
            path_name = endpoint.cls_method_name.replace('_', '-')
            endpoint_path = '{}/{}/'.format(cls.url_prefix, endpoint.endpoint_path)
            paths.append(path(endpoint_path, view, name=path_name))

        return paths

    @classmethod
    def _assert_prefix(cls):
        """
        :raise: TypeError
        """
        if not cls.url_prefix:
            msg = 'The static attribute `url_prefix` must be provided by {}'.format(cls)
            raise TypeError(msg)

    @classmethod
    def _assert_basename(cls):
        """
        :raise: TypeError
        """
        if not cls.url_basename:
            msg = 'The static attribute `url_basename` must be provided by {}'.format(cls)
            raise TypeError(msg)
