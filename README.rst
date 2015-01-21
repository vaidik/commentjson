===========
commentjson
===========

`commentjson` (Comment JSON) is a Python package that helps you create JSON
files with Python and JavaScript style inline comments. Its API is very similar
to the Python standard library's `json`_ module.

.. _`json`: http://docs.python.org/2/library/json.html

.. image:: https://travis-ci.org/vaidik/commentjson.png

Installation
============

    pip install commentjson

Basic Usage
===========

.. code-block:: python

    >>> import commentjson
    >>>
    >>> json_string = """{
    ...     "name": "Vaidik Kapoor", # Person's name
    ...     "location": "Delhi, India", // Person's location
    ...
    ...     # Section contains info about
    ...     // person's appearance
    ...     "appearance": {
    ...         "hair_color": "black",
    ...         "eyes_color": "black",
    ...         "height": "6"
    ...     }
    ... }"""
    >>>
    >>> json_loaded = commentjson.loads(json_string)
    >>> print json_loaded
    {u'appearance': {u'eyes_color': u'black', u'hair_color': u'black', u'height': u'6'}, u'name': u'Vaidik Kapoor', u'location': u'Delhi, India'}

Documentation
=============

Complete documentation can be found `here`_.

.. _`here`: http://commentjson.readthedocs.org/en/latest/

Tests
=====

    python setup.py test

License
=======

See `license`_.

.. _`license`: https://github.com/vaidik/commentjson/blob/master/LICENSE.rst
