__all__ = ['dump', 'dumps', 'load', 'loads', 'JSONLibraryException']

try: # for python 2.x
	from commentjson import dump, dumps, load, loads, JSONLibraryException
except ImportError: # python 3.x
	from .commentjson import dump, dumps, load, loads, JSONLibraryException