import unittest
from app.path_builder import PathBuilder


class TestPathBuilder(unittest.TestCase):
    def test_if_root_empty_raise_error(self):
        with self.assertRaises(ValueError):
            PathBuilder('', 'tests')

    def test_if_tests_folder_empty_raise_error(self):
        with self.assertRaises(ValueError):
            PathBuilder('root', '')

    def test_empty_filename(self):
        builder = PathBuilder('C:\Programming\PHP\ProjectRoot', 'tests')
        self.assertEqual('tests/', builder.build(''))

        builder._root = 'different_root'
        builder._tests = 'diferent_test_folder'
        self.assertEqual('diferent_test_folder/', builder.build(''))

    def test_file_at_root_level(self):
        builder = PathBuilder('C:\\Programming\\PHP\\ProjectRoot', 'tests')
        self.assertEqual('tests/file.py', builder.build('C:\\Programming\\PHP\\ProjectRoot\\file.py'))

    def test_replace_backslashes_with_forward_slashes(self):
        builder = PathBuilder('C:\\ProjectRoot', 'tests/unit')
        self.assertEqual('tests/unit/some/inner/folder/file.py',
                         builder.build('C:\\ProjectRoot\\some\\inner\\folder\\file.py'))

    def test_strip_trailing_slash(self):
        builder = PathBuilder('C:\\Programming\\PHP\\ProjectRoot\\', 'tests')
        self.assertEqual('tests/file2.py', builder.build('C:\\Programming\\PHP\\ProjectRoot\\file2.py'))

