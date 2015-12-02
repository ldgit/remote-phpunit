import unittest

from app.commands.phpunit_command import PHPUnitCommand


class TestPHPUnitCommand(unittest.TestCase):
    def setUp(self):
        # Dependencies
        self._settings = PluginSettingsStub()
        self._sublime = SublimeSpy()

        # SUT
        self._command = PHPUnitCommand(self._sublime, self._settings)

        self._view = ViewStub()
        self._view.file_name_to_return = 'C:/path/to/root/then/path/to/file.php'
        self._settings.root = 'C:/path/to/root'
        self._settings.tests_folder = 'tests/unit'
        self._settings.path_to_phpunit = 'path/to/phpunit'
        self._settings.cl_options = []

    def test_get_command_when_root_defined_in_settings(self):
        self._command.create_run_test_command(self._view)

        self.assertEqual('path/to/phpunit tests/unit/then/path/to/fileTest.php', self._sublime.text_pasted_to_clipboard)

    def test_when_root_empty_in_settings_get_it_from_project_folder(self):
        self._settings.root = ''
        self._view.project_folders = ['C:/path/to/root']

        self._command.create_run_test_command(self._view)

        self.assertEqual('path/to/phpunit tests/unit/then/path/to/fileTest.php', self._sublime.text_pasted_to_clipboard)

    def test_if_empty_root_in_settings_and_no_project_opened_show_error_message_in_status_bar(self):
        self._view.project_folders = []
        self._settings.root = ''

        self._command.create_run_test_command(self._view)

        self.assertEqual(u"Remote PHPUnit: could not find root folder", self._sublime.status_message_string)

    def test_get_command_with_cl_options(self):
        self._settings.cl_options = ['-c config/phpunit.xml', '--colors=\"always\"']

        self._command.create_run_test_command(self._view)

        self.assertEqual(
            'path/to/phpunit -c config/phpunit.xml --colors=\"always\" tests/unit/then/path/to/fileTest.php',
            self._sublime.text_pasted_to_clipboard)

    def test_get_command_for_folder(self):
        dirs = ['C:/path/to/root/then/path/to/folder']
        window = self.get_window_stub('C:/path/to/root')

        self._command.create_run_test_on_folder(dirs, window)

        self.assertEqual(
            'path/to/phpunit tests/unit/then/path/to/folder',
            self._sublime.text_pasted_to_clipboard)

    def test_get_command_for_test_folder(self):
        dirs = ['C:/path/to/root/tests/unit/then/path/to/folder']
        window = self.get_window_stub('C:/path/to/root')

        self._command.create_run_test_on_folder(dirs, window)

        self.assertEqual(
            'path/to/phpunit tests/unit/then/path/to/folder',
            self._sublime.text_pasted_to_clipboard)

    def get_window_stub(self, path_to_root):
        window = WindowStub()
        window.folders = lambda: path_to_root

        return window


class SublimeSpy:
    def __init__(self):
        self.status_message_string = None
        self.text_pasted_to_clipboard = None

    def set_clipboard(self, command):
        self.text_pasted_to_clipboard = command

    def status_message(self, status_message_string):
        self.status_message_string = status_message_string


class PluginSettingsStub:
    pass


class ViewStub:
    def __init__(self):
        self.file_name_to_return = None
        self.project_folders = None

    def file_name(self):
        return self.file_name_to_return

    def window(self):
        window = WindowStub()
        window.folders = self._get_project_folders

        return window

    def _get_project_folders(self):
        return self.project_folders


class WindowStub:
    pass
