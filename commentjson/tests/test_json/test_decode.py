import six
import platform
import unittest

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_decode import TestDecode
else:
    from test.test_json.test_decode import TestDecode

version = platform.sys.version_info


class TestCommentJsonDecode(TestDecode, CommentJsonTest):

    def __init__(self, *args, **kwargs):
        super(TestCommentJsonDecode, self).__init__(*args, **kwargs)

        self.JSONDecodeError = ValueError

        _json = self.json

        class Decoder(object):
            def __init__(self):
                self.decode = _json.loads

        self.json.decoder = Decoder()
        setattr(self.json.decoder, 'JSONDecoder', lambda: Decoder())

    @unittest.skipIf((version.major == 2 or
                      (version.major == 3 and version.minor <= 5)),
                     ('Invalid test case since the the exception raised by'
                      'commentjson is different from the one raised by json '
                      'package.'))
    def test_extra_data(self):
        pass

    @unittest.skipIf((version.major == 2 or
                      (version.major == 3 and version.minor <= 5)),
                     ('Skipping since the test case depends on APIs of JSON '
                      ' package that are not supported by commentjson'))
    def test_keys_reuse(self):
        pass

    @unittest.skipIf(version.major == 2,
                     ('Test case not present in test suite '
                      'for Python 2'))
    def test_invalid_input_type(self):
        try:
            super(TestCommentJsonDecode, self).test_invalid_input_type()
        except AssertionError as e:
            if 'does not match' not in e.args[0]:
                raise e

    @unittest.skipIf(version.major == 2,
                     ('Test case not present in test suite '
                      'for Python 2'))
    def test_string_with_utf8_bom(self):
        try:
            super(TestCommentJsonDecode, self).test_string_with_utf8_bom()
        except AssertionError as e:
            if 'not found' not in e.args[0]:
                raise e

    @unittest.skipIf((version.major == 2 or
                      (version.major == 3 and version.minor <= 5)),
                     ('Invalid test case since the API used in the actual '
                      'test case is not supported by commentjson.'))
    def test_negative_index(self):
        pass
