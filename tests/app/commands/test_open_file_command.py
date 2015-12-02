import unittest

from app.commands.open_file_command import OpenFileCommand


class TestOpenFileCommand(unittest.TestCase):
    def setUp(self):
        self.window = WindowSpy()
        self.settings = PluginSettingsStub()
        self.sublime = SublimeSpy()
        self.os_path = OsPathSpy()

        # SUT
        self.command = OpenFileCommand(self.settings, self.os_path, self.sublime)

    def test_open_source_file(self):
        self.settings.tests_folder = 'tests/unit'

        self.command.open_source_file('C:/path/to/root/tests/unit/path/to/fileTest.php', self.window)

        self.assertEqual('C:/path/to/root/path/to/file.php', self.window.file_to_open)

    def test_open_source_file_works_with_backslashes(self):
        self.settings.tests_folder = 'tests/unit'

        self.command.open_source_file('C:\\path\\to\\root\\tests\\unit\\path\\to\\fileTest.php', self.window)

        self.assertEqual('C:/path/to/root/path/to/file.php', self.window.file_to_open)

    def test_if_source_file_exists_return_true(self):
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = True

        actual = self.command.source_file_exists('C:\\path\\to\\root\\tests\\unit\\path\\to\\fileTest.php')

        self.assertTrue(actual)
        self.assertEqual('C:/path/to/root/path/to/file.php', self.os_path.isfile_received_filepath)

    def test_if_source_file_does_not_exist_return_false(self):
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = False

        self.assertFalse(self.command.source_file_exists('C:/path/to/root/path/to/fileTest.php'))
        self.assertEqual('C:/path/to/root/path/to/file.php', self.os_path.isfile_received_filepath)

    def test_open_file(self):
        self.settings.root = 'C:/path/to/root'
        self.settings.tests_folder = 'tests/unit'

        self.command.open_test_file('C:/path/to/root/path/to/file.php', self.window)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php', self.window.file_to_open)

    def test_correct_file_name_sent_to_os_is_file_method(self):
        self.window.project_root = 'C:/path/to/root'
        self.settings.root = ''
        self.settings.tests_folder = 'tests/unit'

        self.command.test_file_exists('C:/path/to/root/path/to/file.php', self.window)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php', self.os_path.isfile_received_filepath)

    def test_file_exists_ignores_trailing_slash_in_root_path(self):
        self.window.project_root = 'C:/path/to/root/'
        self.settings.root = ''
        self.settings.tests_folder = 'tests/unit'

        self.command.test_file_exists('C:/path/to/root/path/to/file.php', self.window)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php', self.os_path.isfile_received_filepath)

    def test_if_test_file_exists_return_true(self):
        self.settings.root = 'C:/path/to/root/'
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = True

        self.assertTrue(self.command.test_file_exists('C:/path/to/root/path/to/file.php', self.window))

    def test_test_file_exists_returns_true_if_test_file_is_input(self):
        self.settings.root = 'C:/path/to/root/'
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = True

        self.assertTrue(self.command.test_file_exists('C:/path/to/root/tests/unit/path/to/fileTest.php', self.window))
        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php', self.os_path.isfile_received_filepath,
                         'Expected test file filepath as parameter to isfile')

    def test_if_test_file_does_not_exist_return_false(self):
        self.settings.root = 'C:/path/to/root/'
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = False

        self.assertFalse(self.command.test_file_exists('C:/path/to/root/path/to/file.php', self.window))

    def test_replace_back_slashes_with_forward_slashes(self):
        self.window.project_root = 'C:\\path\\to\\root'
        self.settings.root = ''
        self.settings.tests_folder = 'tests\\unit'

        self.command.test_file_exists('C:\\path\\to\\root\\path\\to\\file.php', self.window)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php', self.os_path.isfile_received_filepath)


class PluginSettingsStub:
    pass


class WindowSpy:
    def __init__(self):
        self.file_to_open = None
        self.project_root = None

    def folders(self):
        return [self.project_root]

    def open_file(self, file_to_open):
        self.file_to_open = file_to_open


class OsPathSpy:
    def __init__(self):
        self.is_file_returns = None
        self.isfile_received_filepath = None

    def isfile(self, filepath):
        self.isfile_received_filepath = filepath

        return self.is_file_returns


class SublimeSpy:
    pass
