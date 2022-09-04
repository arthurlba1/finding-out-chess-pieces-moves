# !.usr.bin.env python3
# -*- coding: utf-8 -*-

"""Serializes a object to JSON supported type"""

import json

from rest_framework import renderers


class JSONRenderer(renderers.JSONRenderer, json.JSONEncoder):
    """Serializes a object to JSON supported type"""

    def default(self, obj):
        """
        :param base.viewset.json_serializable.JSONSerializable obj:
        :return dict:
        """
        return obj.to_dto()

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        :param base.api_view.json_serializable.JSONSerializable data:
        :param list accepted_media_type:
        :param object renderer_context:
        :return bytes:
        """
        ret = json.dumps(data, cls=JSONRenderer)

        # Fully escape \u2028 and \u2029 to ensure we output JSON
        # that is a strict javascript subset.
        # See: http://timelessrepo.com/json-isnt-a-javascript-subset
        ret = ret.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')

        return ret.encode()
