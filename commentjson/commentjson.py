try:
    import json
except ImportError:
    # If python version is 2.5 or less, use simplejson
    import simplejson as json

import re
import traceback


class JSONLibraryException(Exception):
    ''' Exception raised when the JSON library in use raises an exception i.e.
    the exception is not caused by `commentjson` and only caused by the JSON
    library `commentjson` is using.

    .. note::

        As of now, ``commentjson`` supports only standard library's ``json``
        module. It might start supporting other widely-used contributed JSON
        libraries in the future.
    '''

    def __init__(self, json_error=""):
        tb = traceback.format_exc()
        tb = '\n'.join(' ' * 4 + line_ for line_ in tb.split('\n'))
        message = [
            'JSON Library Exception\n',
            ('Exception thrown by JSON library (json): '
             '\033[4;37m%s\033[0m\n' % json_error),
            '%s' % tb,
        ]
        Exception.__init__(self, '\n'.join(message))


def loads(text, **kwargs):
    ''' Deserialize `text` (a `str` or `unicode` instance containing a JSON
    document with Python or JavaScript like comments) to a Python object.

    :param text: serialized JSON string with or without comments.
    :param kwargs: all the arguments that `json.loads <http://docs.python.org/
                   2/library/json.html#json.loads>`_ accepts.
    :raises: commentjson.JSONLibraryException
    :returns: dict or list.
    '''
    regex = r'\s*(#|\/{2}).*$'
    regex_inline = r'(:?(?:\s)*([A-Za-z\d\.{}]*)|((?<=\").*\"),?)(?:\s)*(((#|(\/{2})).*)|)$'
    lines = text.split('\n')
    excluded = []

    for index, line in enumerate(lines):
        if re.search(regex, line):
            if re.search(r'^' + regex, line, re.IGNORECASE):
                excluded.append(lines[index])
            elif re.search(regex_inline, line):
                lines[index] = re.sub(regex_inline, r'\1', line)

    for line in excluded:
        lines.remove(line)

    try:
        return json.loads('\n'.join(lines), **kwargs)
    except Exception as e:
        raise JSONLibraryException(str(e))


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
        raise JSONLibraryException(str(e))


def load(fp, **kwargs):
    ''' Deserialize `fp` (a `.read()`-supporting file-like object containing
    a JSON document with Python or JavaScript like comments) to a Python object.

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
        raise JSONLibraryException(str(e))


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
        raise JSONLibraryException(str(e))
