import six
import platform
import unittest

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_encode_basestring_ascii import TestEncodeBasestringAscii
else:
    from test.test_json.test_encode_basestring_ascii import TestEncodeBasestringAscii

version = platform.sys.version_info


class TestCommentJsonEncodeBasestringAscii(TestEncodeBasestringAscii, CommentJsonTest):

    @unittest.skip('Skip this test since commentjson does not support the API '
                   'used in the test case.')
    def test_encode_basestring_ascii(self):
        pass
