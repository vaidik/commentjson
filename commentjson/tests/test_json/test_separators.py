import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_separators import TestSeparators
else:
    from test.test_json.test_separators import TestSeparators

version = platform.sys.version_info


class TestCommentJsonSeparators(TestSeparators, CommentJsonTest):

    pass
