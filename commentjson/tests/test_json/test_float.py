import six
import platform
import unittest

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_float import TestFloat
else:
    from test.test_json.test_float import TestFloat

version = platform.sys.version_info


class TestCommentJsonFloat(TestFloat, CommentJsonTest):

    @unittest.skip('Infinity as a value is not supported yet')
    def test_allow_nan(self):
        pass
