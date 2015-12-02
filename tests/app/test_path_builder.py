import unittest
from app.path_builder import PathBuilder


class TestPathBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = PathBuilder()

    def test_with_empty_root_and_test_folder(self):
        self.assertEqual('a_fileTest.php', self.builder.build('a_file.php', '', ''))

    def test_empty_root(self):
        self.assertEqual('tests/unit/a_fileTest.php', self.builder.build('a_file.php', '', 'tests/unit/'))
        
    def test_backslashes_in_tests_folder_path(self):
        self.assertEqual('tests/unit/a_fileTest.php', self.builder.build('a_file.php', '', 'tests\\unit\\'))

    def test_add_trailing_slash_to_tests_folder_if_missing(self):
        self.assertEqual('tests/unit/a_fileTest.php', self.builder.build('a_file.php', '', 'tests/unit'))
        self.assertEqual('tests/unit/a_fileTest.php', self.builder.build('a_file.php', '', 'tests\\unit'))
        
    def test_strip_root_from_filepath(self):
        root = 'C:\\root_folder'
        file = 'C:\\root_folder' + '\\a_file.php'
        self.assertEqual('a_fileTest.php', self.builder.build(file, root, ''))

    def test_file_deeper_in_folder_structure(self):
        file = 'C:\\root_folder\\some_folder\\a_file.php'
        root = 'C:\\root_folder'
        self.assertEqual('some_folder/a_fileTest.php', self.builder.build(file, root, ''))
        
    def test_all_together(self):
        file = 'C:\\root_folder\\some_folder\\a_file.php'
        root = 'C:\\root_folder'
        tests = 'tests/unit'
        self.assertEqual('tests/unit/some_folder/a_fileTest.php', self.builder.build(file, root, tests))
    
    def test_if_filepath_does_not_end_in_php_do_not_append_Test(self):
        self.assertEqual('a_folder', self.builder.build('a_folder', '', ''))

    def test_filepath_does_not_end_in_php(self):
        self.assertEqual('unit/tests/a_folder', self.builder.build('root/path/a_folder', 'root/path', 'unit/tests'))

    def test_if_filepath_is_in_test_folder_do_not_appent_test_folder_to_path(self):
        self.assertEqual('unit/tests/a_folder',
                         self.builder.build('root/path/unit/tests/a_folder', 'root/path', 'unit/tests'))
        
    def test_do_not_append_test_folder_path_and_test_suffix_if_file_already_in_test_folder(self):
        file = 'C:\\root_folder\\tests\\unit\\some_folder\\a_fileTest.php'
        root = 'C:\\root_folder'
        tests = 'tests/unit'
        self.assertEqual('tests/unit/some_folder/a_fileTest.php', self.builder.build(file, root, tests))
