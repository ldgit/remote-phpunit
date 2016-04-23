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

    def test_if_tests_folder_is_not_unit_test_folder_assume_there_is_unit_subfolder_in_tests_folder(self):
        file = 'C:/path/to/root/path/to/file/a_file.php'
        root = 'C:/path/to/root'
        path_to_tests = 'tests'

        self.assertEqual('tests/unit/path/to/file/a_fileTest.php', self.builder.build(file, root, path_to_tests))

    def test_if_file_inside_tests_folder_just_use_its_relative_path(self):
        file = 'C:/path/to/root/tests_folder/path/to/file/a_fileTest.php'
        root = 'C:/path/to/root'
        path_to_tests = 'tests_folder'

        self.assertEqual('tests_folder/path/to/file/a_fileTest.php', self.builder.build(file, root, path_to_tests))

    def test_all_together(self):
        file = 'C:\\root_folder\\some_folder\\a_file.php'
        root = 'C:\\root_folder'
        tests = 'tests/unit'
        self.assertEqual('tests/unit/some_folder/a_fileTest.php', self.builder.build(file, root, tests))

    def test_if_filepath_is_a_folder_do_not_append_Test(self):
        self.assertEqual('a_folder', self.builder.build('a_folder', '', ''))

    def test_filepath_is_a_folder(self):
        self.assertEqual('tests/unit/a_folder', self.builder.build('path/to/root/a_folder', 'path/to/root', 'tests/unit'))

    def test_filepath_is_in_test_folder(self):
        self.assertEqual('tests/unit/a_folder',
                         self.builder.build('path/to/root/tests/unit/a_folder', 'path/to/root', 'tests/unit'))
        self.assertEqual('tests/unit',
                         self.builder.build('path/to/root/tests/unit', 'path/to/root', 'tests/unit'))
        self.assertEqual('tests/unit',
                         self.builder.build(u'C:\\path\\to\\root\\tests\\unit', u'C:\\path\\to\\root', u'tests/unit'),
                         'with backslashes')

    def test_regression_when_root_already_ends_with_slash(self):
        file = 'C:\\path\\to\\root\\path\\to\\file\\a_file.php'
        root = 'C:/path/to/root/'
        tests = 'tests/unit'
        self.assertEqual('tests/unit/path/to/file/a_fileTest.php', self.builder.build(file, root, tests))

    def test_do_not_append_test_folder_path_and_test_suffix_if_file_already_in_test_folder(self):
        file = 'C:\\root_folder\\tests\\unit\\some_folder\\a_fileTest.php'
        root = 'C:\\root_folder'
        tests = 'tests/unit'
        self.assertEqual('tests/unit/some_folder/a_fileTest.php', self.builder.build(file, root, tests))
