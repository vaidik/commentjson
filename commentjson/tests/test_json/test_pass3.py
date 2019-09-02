import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_pass3 import TestPass3
else:
    from test.test_json.test_pass3 import TestPass3

version = platform.sys.version_info


class TestCommentJsonPass3(TestPass3, CommentJsonTest):

    pass
