import six
import platform
import unittest

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_unicode import TestUnicode
else:
    from test.test_json.test_unicode import TestUnicode

version = platform.sys.version_info


class TestCommentJsonUnicode(TestUnicode, CommentJsonTest):

    @unittest.skipIf(version.major == 3 and version.minor <= 5,
                     ('Invalid test case since the API used in the actual '
                      'test case is not supported by commentjson.'))
    def test_encoding1(self):
        pass

    @unittest.skipIf((version.major == 2 or
                      (version.major == 3 and version.minor <= 5)),
                     'Invalid test case for Python 2.7 and 3+ to 3.5.')
    def test_bytes_decode(self):
        TestCommentJsonUnicode.__bases__[0].test_bytes_decode(self)
