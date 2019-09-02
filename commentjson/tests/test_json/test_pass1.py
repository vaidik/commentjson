import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_pass1 import TestPass1
else:
    from test.test_json.test_pass1 import TestPass1

version = platform.sys.version_info


class TestCommentJsonPass1(TestPass1, CommentJsonTest):

    pass
