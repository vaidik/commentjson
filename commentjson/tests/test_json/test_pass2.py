import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_pass2 import TestPass2
else:
    from test.test_json.test_pass2 import TestPass2

version = platform.sys.version_info


class TestCommentJsonPass2(TestPass2, CommentJsonTest):

    pass
