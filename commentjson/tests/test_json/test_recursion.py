import six
import platform
import unittest

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_recursion import TestRecursion
else:
    from test.test_json.test_recursion import TestRecursion

version = platform.sys.version_info


class TestCommentJsonRecursion(TestRecursion, CommentJsonTest):

    @unittest.skipIf(version.major == 3,
                     ('Invalid test case since the API used in the actual '
                      'test case is not supported by commentjson.'))
    def test_defaultrecursion(self):
        pass

    @unittest.skipIf(version.major == 3,
                     ('Invalid test case since the API used in the actual '
                      'test case is not supported by commentjson.'))
    def test_endless_recursion(self):
        pass
