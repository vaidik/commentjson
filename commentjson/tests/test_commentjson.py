try:
    import json
except ImportError:
    import simplejson as json

import commentjson
import os
import unittest

from six import iteritems


class TestCommentJson(unittest.TestCase):

    def setUp(self):
        self.test_json = {}
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.files = ('sample', 'line_comment', 'inline_last_float',
                      'inline_last_int', 'nested_object', 'string_with_hash',
                      'string_with_inline_comment',
                      'inline_has_special_characters',
                      'array_with_hash',
                      'inline_last_quote')

        for file_ in self.files:
            fpath = os.path.join(self.path, file_)

            with open('%s-uncommented.json' % fpath) as fp:
                uncommented = fp.read()
            with open('%s-commented.json' % fpath) as fp:
                commented = fp.read()

            self.test_json.update({
                file_: {
                    'uncommented': uncommented,
                    'commented': commented,
                },
            })

    def tearDown(self):
        test_file_path = os.path.join(self.path, 'test.json')
        if os.path.exists(test_file_path):
            os.unlink(test_file_path)

    def test_dumping_parsing_simple_string(self):
        string = '//'
        self.assertEqual(commentjson.loads(commentjson.dumps(string)), string)

        string = '#'
        self.assertEqual(commentjson.loads(commentjson.dumps(string)), string)

    def test_dumps(self):
        test_dict = dict(a=1, b=2)
        c_dump = commentjson.dumps(test_dict)
        j_dump = json.dumps(test_dict)
        assert c_dump, j_dump

    def test_dumps_with_kwargs(self):
        test_dict = dict(a=1, b=2)
        test_kwargs = dict(indent=4)

        c_dump = commentjson.dumps(test_dict, **test_kwargs)
        j_dump = json.dumps(test_dict, **test_kwargs)
        assert c_dump, j_dump

    def test_dumps_throws_exception(self):
        class Unserializable:
            pass
        self.assertRaises(commentjson.JSONLibraryException, commentjson.dumps,
                          Unserializable)

    def test_loads(self):
        for index, test_json_ in iteritems(self.test_json):
            commented = test_json_['commented']
            uncommented = test_json_['uncommented']
            self.assertEqual(
                commentjson.loads(commented),
                json.loads(uncommented),
                'Failed for test: %s' % test_json_['commented'])

    def test_loads_with_kwargs(self):
        def test_hook(loaded_dict):
            return {}
        commented = self.test_json['sample']['commented']
        test_kwargs = dict(object_hook=test_hook)

        c_load = commentjson.loads(commented, **test_kwargs)

        # make sure that object_hook did its work
        assert c_load == {}

    def test_loads_throws_exception(self):
        self.assertRaises(commentjson.ParserException, commentjson.loads,
                          'Unserializable text')

    def test_dump(self):
        test_dict = dict(a=1, b=2)

        wfp = open(os.path.join(self.path, 'test.json'), 'w')
        commentjson.dump(test_dict, wfp)
        wfp.close()

        rfp = open(os.path.join(self.path, 'test.json'), 'r')
        j_dump = json.dumps(test_dict)

        assert rfp.read(), j_dump
        rfp.close()

    def test_dump_with_kwargs(self):
        test_dict = dict(a=1, b=2)
        test_kwargs = dict(indent=4)

        wfp = open(os.path.join(self.path, 'test.json'), 'w')
        commentjson.dump(test_dict, wfp, **test_kwargs)
        wfp.close()

        rfp = open(os.path.join(self.path, 'test.json'), 'r')
        j_dump = json.dumps(test_dict, **test_kwargs)
        c_dump = rfp.read()

        assert c_dump == j_dump, c_dump
        rfp.close()

    def test_dump_throws_exception(self):
        class Unserializable:
            pass
        fp = open(os.path.join(self.path, 'test.json'), 'w')
        self.assertRaises(commentjson.JSONLibraryException, commentjson.dump,
                          Unserializable, fp)
        fp.close()

    def test_load(self):
        for file_ in self.files:
            rfp = open(os.path.join(self.path, '%s-commented.json' % file_),
                       'r')
            uncommented = self.test_json[file_]['uncommented']
            assert commentjson.load(rfp) == json.loads(uncommented)
            rfp.close()

    def test_load_with_kwargs(self):
        def test_hook(loaded_dict):
            return {}

        test_kwargs = dict(object_hook=test_hook)
        rfp = open(os.path.join(self.path, 'sample-commented.json'), 'r')

        self.assertEqual(commentjson.load(rfp, **test_kwargs), {})
        rfp.close()

    def test_load_throws_exception(self):
        wfp = open(os.path.join(self.path, 'test.json'), 'w')
        wfp.write('Unserializable text.')
        wfp.close()

        rfp = open(os.path.join(self.path, 'test.json'), 'r')
        self.assertRaises(commentjson.JSONLibraryException, commentjson.load,
                          rfp)
        rfp.close()


if __name__ == '__main__':
    unittest.main()
