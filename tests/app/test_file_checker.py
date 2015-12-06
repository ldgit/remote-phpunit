import unittest
from app.file_checker import FileChecker


class TestFileChecker(unittest.TestCase):
    def test_is_php_file_returns_false_for_empty_string(self):
        self.assertFalse(self.file_checker.is_php_file(''))

    def test_is_php_file_returns_false_if_file_does_not_have_php_extension(self):
        self.assertFalse(self.file_checker.is_php_file('a_file.py'))
        self.assertFalse(self.file_checker.is_php_file('a_.php_file.py'))
        self.assertFalse(self.file_checker.is_php_file('.php_a_file.py'))
        self.assertFalse(self.file_checker.is_php_file('C:/path/to/directory'))

    def test_is_php_file_returns_true_for_php_file_extension(self):
        self.assertTrue(self.file_checker.is_php_file('a_file.php'))
        self.assertTrue(self.file_checker.is_php_file('C:/path/to/file.php'))

    def test_is_php_file_is_case_insensitive(self):
        self.assertTrue(self.file_checker.is_php_file('A_FILE.PHP'))
        self.assertFalse(self.file_checker.is_php_file('A_FILE.PY'))

    def setUp(self):
        self.file_checker = FileChecker()
