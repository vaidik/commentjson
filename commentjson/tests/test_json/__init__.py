import unittest

import commentjson


class CommentJsonTest(unittest.TestCase):
    json = commentjson
    loads = staticmethod(commentjson.loads)
    dumps = staticmethod(commentjson.dumps)
