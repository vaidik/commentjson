import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_dump import TestDump
else:
    from test.test_json.test_dump import TestDump

version = platform.sys.version_info


class TestCommentJsonDump(TestDump, CommentJsonTest):

    pass
