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
        
    #
    # def test_if_tests_folder_empty_raise_error(self):
    #     with self.assertRaises(ValueError):
    #         self.builder.build('', 'root', '')
    #
    # def test_empty_filename(self):
    #     self.assertEqual('tests/', self.builder.build('', 'C:\Programming\PHP\ProjectRoot', 'tests'))
    #
    #     self.assertEqual('different_test_folder/', self.builder.build('', 'different_root', 'different_test_folder'))
    #
    # def test_file_at_root_level(self):
    #     path = self.builder.build('C:\\Programming\\PHP\\ProjectRoot\\file.py', 'C:\\Programming\\PHP\\ProjectRoot',
    #                               'tests')
    #
    #     self.assertEqual('tests/file.py', path)
    #
    # def test_replace_backslashes_with_forward_slashes(self):
    #     path = self.builder.build('C:\\ProjectRoot\\some\\inner\\folder\\file.py', 'C:\\ProjectRoot', 'tests/unit')
    #
    #     self.assertEqual('tests/unit/some/inner/folder/file.py', path)
    #
    # def test_strip_trailing_slash(self):
    #     path = self.builder.build('C:\\Programming\\PHP\\ProjectRoot\\file2.py', 'C:\\Programming\\PHP\\ProjectRoot\\',
    #                               'tests')
    #
    #     self.assertEqual('tests/file2.py', path)
