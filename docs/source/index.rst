.. commentjson documentation master file, created by
   sphinx-quickstart on Tue Sep 10 14:48:22 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

commentjson - Add comments in JSON files
========================================

``commentjson`` is a Python library that lets you have comments in your JSON
files. Its API is very similar to the Python Standard library's
`json <http://docs.python.org/2/library/json.html>`_ module.

What does commentjson do?
-------------------------

``commentjson`` allows you to deserialize JSON files with Pythons style
comments in them. ``commentjson``'s API is the same as the standard library's
`json <http://docs.python.org/2/library/json.html>`_ module. If you are using
or like using JSON for configuration files, ``commentjson`` can be very handy.

You may put comments in your JSON files like so:

.. code-block:: json

    {
        "name": "Vaidik Kapoor", # Person's name
        "location": "Delhi, India",

        # Section contains info about person's appearance
        "appearance": {
            "hair_color": "black",
            "eyes_color": "black",
            "height": "6"
        }
    }

Installation
------------

``pip install commentjson``

Basic Usage
-----------

Since ``commentjson``'s API is the same as standard libraries
`json <http://docs.python.org/2/library/json.html>`_ module, it is extremely
simple to use ``commentjson``. You don't have to do anything new to use
``commentjson``. Here is what you have to do:

1. Write your JSON files by hand or use standard library's
   `json <http://docs.python.org/2/library/json.html>`_ module or
   ``commentjson`` to create a new JSON file.
2. Open the JSON file in your text editor and add comments the same way you
   would in Python (using ``#`` and not docstrings).
3. Use ``commentjson``'s ``loads`` or ``load`` method to deserialize the file
   just like how you would use
   `json <http://docs.python.org/2/library/json.html>`_ module to parse a
   normal JSON string without comments. ``load`` and ``loads`` will return you
   a Python object.

.. code-block:: python

   >>> import commentjson
   >>>
   >>> json_string = """{
   ...     "name": "Vaidik Kapoor", # Person's name
   ...     "location": "Delhi, India",
   ...
   ...     # Section contains info about person's appearance
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

API Documentation
-----------------

.. autofunction:: commentjson.loads

.. autofunction:: commentjson.dumps

.. autofunction:: commentjson.load

.. autofunction:: commentjson.dump

.. autoexception:: commentjson.JSONLibraryException

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

