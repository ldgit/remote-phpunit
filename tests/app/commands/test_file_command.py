import unittest

from app.commands.file_command import FileCommand


class TestFileCommand(unittest.TestCase):
    def setUp(self):
        self.window = WindowSpy()
        self.settings = PluginSettingsStub()
        self.sublime = SublimeSpy()
        self.os_path = OsPathSpy()

        # SUT
        self.command = FileCommand(self.settings, self.os_path, self.sublime)

    def test_open_source_file(self):
        self.settings.tests_folder = 'tests/unit'
        self.command.open_source_file('C:/path/to/root/tests/unit/path/to/fileTest.php', self.window)
        self.assertEqual('C:/path/to/root/path/to/file.php', self.window.file_to_open)

    def test_open_source_file_works_with_backslashes(self):
        self.settings.tests_folder = 'tests/unit'
        self.command.open_source_file('C:\\path\\to\\root\\tests\\unit\\path\\to\\fileTest.php', self.window)
        self.assertEqual('C:/path/to/root/path/to/file.php', self.window.file_to_open)

    def test_open_source_file_works_for_network_paths(self):
        self.settings.tests_folder = 'tests'
        self.command.open_source_file('\\\\server\\dev\\root\\tests\\unit\\Service\\SearchParametersMapperTest.php',
                                      self.window)
        self.assertEqual('\\\\server\\dev\\root\\Service\\SearchParametersMapper.php', self.window.file_to_open)

    def test_open_source_file_works_for_network_paths_and_complex_tests_folder(self):
        self.settings.tests_folder = 'tests/unit'
        self.command.open_source_file('\\\\server\\dev\\root\\tests\\unit\\Service\\SearchParametersMapperTest.php',
                                      self.window)
        self.assertEqual('\\\\server\\dev\\root\\Service\\SearchParametersMapper.php', self.window.file_to_open)

    def test_open_source_file_when_tests_folder_is_not_unit_test_folder(self):
        self.settings.root = 'C:/path/to/root'
        self.settings.tests_folder = 'tests_folder'

        self.command.open_source_file('C:/path/to/root/tests_folder/unit/path/to/fileTest.php', self.window)

        self.assertEqual('C:/path/to/root/path/to/file.php', self.window.file_to_open)

    def test_open_source_file_remove_only_first_appearance_of_tests_folder_in_path(self):
        self.settings.root = 'C:/path/to/root'
        self.settings.tests_folder = 'tests'

        self.command.open_source_file('C:/path/to/root/tests/unit/path/to/tests/fileTest.php', self.window)

        self.assertEqual('C:/path/to/root/path/to/tests/file.php', self.window.file_to_open)

    def test_open_source_file_when_tests_folder_is_not_unit_test_folder_remove_only_unit_folder_after_test_path(self):
        self.settings.root = 'C:/path/to/root'
        self.settings.tests_folder = 'tests_folder'

        self.command.open_source_file('C:/path/to/root/tests_folder/unit/path/to/unit/fileTest.php', self.window)

        self.assertEqual('C:/path/to/root/path/to/unit/file.php', self.window.file_to_open)

    def test_if_source_file_exists_return_true(self):
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = True

        actual = self.command.source_file_exists('C:\\path\\to\\root\\tests\\unit\\path\\to\\fileTest.php')

        self.assertTrue(actual)
        self.assertEqual('C:/path/to/root/path/to/file.php', self.os_path.isfile_received_filepath)

    def test_source_file_does_not_exist_if_file_already_is_a_source_file(self):
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = True

        actual = self.command.source_file_exists('root\path\src\Gallery\ImageType.php')

        self.assertFalse(actual)

    def test_if_source_file_does_not_exist_return_false(self):
        self.settings.tests_folder = 'tests/unit'
        self.os_path.is_file_returns = False

        self.assertFalse(self.command.source_file_exists('C:/path/to/root/path/to/fileTest.php'))
        self.assertEqual('C:/path/to/root/path/to/file.php', self.os_path.isfile_received_filepath)

    def test_if_source_file_is_none_return_false(self):
        """ This case is possible when currently opened tab in sublime is untitled (i.e. not yet created) file """
        self.assertFalse(self.command.source_file_exists(None))

    def test_if_test_file_is_none_return_false(self):
        """ This case is possible when currently opened tab in sublime is untitled (i.e. not yet created) file """
        self.settings.root = 'C:/path/to/root'
        self.settings.tests_folder = 'tests/unit'
        self.assertFalse(self.command.test_file_exists(None, self.window))

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
