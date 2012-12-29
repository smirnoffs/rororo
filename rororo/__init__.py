"""
======
rororo
======

Functional nano web-framework built on top of `WebOb <http://webob.org/>`_,
`routr <http://routr.readthedocs.org>`_ and `Jinja <http://jinja.pocoo.org>`_.

"""

from routr import (
    DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, TRACE, include, plug, route
)
from routr.static import static
from routrschema import RequestParams, form, json_body, qs
from schemify import ValidationError, anything, opt, validate
from webob.request import Request
from webob.response import Response

from .app import config, create_app, renderer
from .manager import manage
