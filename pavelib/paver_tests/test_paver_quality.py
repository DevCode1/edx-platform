import os
import mock
from mock import patch, MagicMock
import unittest
import pavelib.quality
import StringIO
import tempfile
import os
from ddt import ddt, file_data


@ddt
class TestPaverQuality(unittest.TestCase):

    def setUp(self):
        self.f = tempfile.NamedTemporaryFile(delete=False)
        self.f.close()

    def test_pylint_parser_other_string(self):
        with open(self.f.name, 'w') as f:
            f.write("hello")
        num = pavelib.quality._count_pylint_violations(f.name)
        self.assertEqual(num, 0)

    @file_data('quality_test_list.json')
    def test_pylint_parser_count_violations(self, value):
    # Tests:
    #     * Different types of violations
    #     * One violation covering multiple lines
        with open(self.f.name, 'w') as f:
            f.write(value)
        num = pavelib.quality._count_pylint_violations(f.name)
        self.assertEqual(num, 1)


    def tearDown(self):
        os.remove(self.f.name)