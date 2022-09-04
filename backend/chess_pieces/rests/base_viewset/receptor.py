"""Responsible for handle request/responses"""

import traceback
from functools import wraps

from django.db.models.fields.files import FieldFile
from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


class Receptor:

    @classmethod
    def request_handler(cls, method):

        """
        :param function method:
        :return function:
        """
        @wraps(method)
        def parameters(*args, **kwargs) -> Response:
            """
            :param list args:
            :param dict kwargs:
            :return Response:
            """
            return cls._request_handler(method, *args, **kwargs)

        return parameters

    @classmethod
    def endpoint(cls, path, http_method=None):
        """
        :param str path:
        :param str http_method:
        :return function:
        """
        def method_wrapper(method):
            """
            :param function method:
            :return function:
            """
            @wraps(method)
            def parameters(*args, **kwargs) -> Response:
                """
                :param list args:
                :param dict kwargs:
                :return Response:
                """
                return cls._request_handler(method, *args, **kwargs)

            return parameters

        return method_wrapper

    @classmethod
    def _request_handler(cls, method, *args, **kwargs) -> Response:
        """
        :param function method:
        :param list args:
        :param dict kwargs:
        :return Response:
        """
        try:
            data = method(*args, **kwargs)
            if type(data) == Response:
                response = data
            else:
                response = cls._build_ok_response(data)
        except ValidationError as exc:
            raise exc
        except Exception as exc:
            traceback.print_exc()
            response = cls._build_error_response(exc.args[0])

        return response

    @classmethod
    def _build_ok_response(cls, body) -> Response:
        """
        :param any body:
        """
        if body and type(body) == FieldFile:
            response = FileResponse(body)

        elif body:
            response = Response(data=body)

        else:
            response = Response()

        response.status_code = status.HTTP_200_OK

        return response

    @classmethod
    def _build_error_response(cls, body) -> Response:
        """
        :param any body:
        """
        return Response(data=body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
