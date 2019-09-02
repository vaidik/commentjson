import six
import platform

from . import CommentJsonTest

if six.PY2:
    from json.tests.test_indent import TestIndent
else:
    from test.test_json.test_indent import TestIndent

version = platform.sys.version_info


class TestCommentJsonIndent(TestIndent, CommentJsonTest):

    pass
