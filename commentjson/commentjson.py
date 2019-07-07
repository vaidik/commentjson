#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Add JavaScript or Python style comments in JSON.

commentjson (Comment JSON) is a Python package that helps you create JSON files
with Python and JavaScript style inline comments. Its API is very similar to
the Python standard library’s json module.

"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import re
import six
import traceback

try:
    import json
except ImportError:
    # If python version is 2.5 or less, use simplejson
    import simplejson as json


import lark

from lark import Lark
from lark.reconstruct import Reconstructor


parser = Lark('''
    ?start: value
    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null
    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : string ":" value
    string : ESCAPED_STRING

    COMMENT: /(#|\/\/)[^\\n]*/

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    %ignore COMMENT
''', start='start')

serializer = Reconstructor(parser)


class BaseException(Exception):
    ''' Base exception to be implemented and raised while handling exceptions
    raised by libraries used in `commentjson`.

    Sets message of self in a way that it clearly calls out that the exception
    was raised by another library, along with the entire stacktrace of the
    exception raised by the other library.
    '''

    def __init__(self, exc):
        if self.library is None:
            raise NotImplementedError(
                'Value of library must be set in the '
                'inherited exception class.')

        tb = traceback.format_exc()
        tb = '\n'.join(' ' * 4 + line_ for line_ in tb.split('\n'))

        error = None
        try:
            error = exc.msg
        except AttributeError:
            try:
                error = exc.message
            except AttributeError:
                error = str(exc)

        self.message = '\n'.join([
            'JSON Library Exception\n',
            ('Exception thrown by library (%s): '
             '\033[4;37m%s\033[0m\n' % (self.library, error)),
            '%s' % tb,
        ])
        Exception.__init__(self, self.message)


class ParserException(BaseException):
    '''Exception raised when the `lark` raises an exception i.e.
    the exception is not caused by `commentjson` and caused by the use of
    `lark` in `commentjson`.
    '''

    library = 'lark'


class JSONLibraryException(BaseException):
    '''Exception raised when the `json` raises an exception i.e.
    the exception is not caused by `commentjson` and caused by the use of
    `json` in `commentjson`.

    .. note::

        As of now, ``commentjson`` supports only standard library's ``json``
        module. It might start supporting other widely-used contributed JSON
        libraries in the future.
    '''

    library = 'json'


def loads(text, **kwargs):
    ''' Deserialize `text` (a `str` or `unicode` instance containing a JSON
    document with Python or JavaScript like comments) to a Python object.

    :param text: serialized JSON string with or without comments.
    :param kwargs: all the arguments that `json.loads <http://docs.python.org/
                   2/library/json.html#json.loads>`_ accepts.
    :returns: dict or list.
    '''

    if six.PY2:
        text = six.text_type(text, 'utf-8')

    regex = r'\s*(#|\/{2}).*$'
    regex_inline = r'(:?(?:\s)*([A-Za-z\d\.{}]*)|((?<=\").*\"),?)(?:\s)*(((#|(\/{2})).*)|)$'
    lines = text.split('\n')

    for index, line in enumerate(lines):
        if re.search(regex, line):
            if re.search(r'^' + regex, line, re.IGNORECASE):
                lines[index] = ""
            elif re.search(regex_inline, line):
                lines[index] = re.sub(regex_inline, r'\1', line)

    try:
        parsed = parser.parse(text)
        final_text = serializer.reconstruct(parsed)
    except lark.exceptions.UnexpectedCharacters:
        raise ParserException('Unable to parse text')

    try:
        return json.loads(final_text, **kwargs)
    except Exception as e:
        raise JSONLibraryException(e)


def dumps(obj, **kwargs):
    ''' Serialize `obj` to a JSON formatted `str`. Accepts the same arguments
    as `json` module in stdlib.

    :param obj: a JSON serializable Python object.
    :param kwargs: all the arguments that `json.dumps <http://docs.python.org/
                   2/library/json.html#json.dumps>`_ accepts.
    :raises: commentjson.JSONLibraryException
    :returns str: serialized string.
    '''

    try:
        return json.dumps(obj, **kwargs)
    except Exception as e:
        raise JSONLibraryException(e)


def load(fp, **kwargs):
    ''' Deserialize `fp` (a `.read()`-supporting file-like object containing a
    JSON document with Python or JavaScript like comments) to a Python object.

    :param fp: a `.read()`-supporting file-like object containing a JSON
               document with or without comments.
    :param kwargs: all the arguments that `json.load <http://docs.python.org/
                   2/library/json.html#json.load>`_ accepts.
    :raises: commentjson.JSONLibraryException
    :returns: dict or list.
    '''

    try:
        return loads(fp.read(), **kwargs)
    except Exception as e:
        raise JSONLibraryException(e)


def dump(obj, fp, **kwargs):
    ''' Serialize `obj` as a JSON formatted stream to `fp` (a
    `.write()`-supporting file-like object). Accepts the same arguments as
    `json` module in stdlib.

    :param obj: a JSON serializable Python object.
    :param fp: a `.read()`-supporting file-like object containing a JSON
               document with or without comments.
    :param kwargs: all the arguments that `json.dump <http://docs.python.org/
                   2/library/json.html#json.dump>`_ accepts.
    :raises: commentjson.JSONLibraryException
    '''

    try:
        json.dump(obj, fp, **kwargs)
    except Exception as e:
        raise JSONLibraryException(e)
