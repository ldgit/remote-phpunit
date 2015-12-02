import unittest

from app.commands.create_file_command import CreateFileCommand


class TestCreateFileCommand(unittest.TestCase):
    def test_SUT_has_file_creator(self):
        from app.file_creator import FileCreator
        command = CreateFileCommand('sublime dummy', self._plugin_settings)

        self.assertTrue(hasattr(command, '_get_file_creator'))
        self.assertTrue(isinstance(command._get_file_creator(), FileCreator),
                        '_get_file_creator must return instance of FileCreator class')

    def test_create_file_sends_correct_path_to_file_creator__root_read_from_settings(self):
        self._plugin_settings.root = 'C:/path/to/root'
        self._view.project_folders = []

        self._command.create_test_file(self._view)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php',
                         self._command.file_creator_instance.path_to_create)

    def test_create_file_sends_correct_path_to_file_creator__root_read_from_sublime_view(self):
        self._plugin_settings.root = ''
        self._view.project_folders = ['C:/path/to/root']

        self._command.create_test_file(self._view)

        self.assertEqual('C:/path/to/root/tests/unit/path/to/fileTest.php',
                         self._command.file_creator_instance.path_to_create)

    def setUp(self):
        self._plugin_settings = PluginSettingsStub()
        self._plugin_settings.tests_folder = 'tests/unit'
        self._view = ViewStub()
        self._view.file_name = lambda: 'C:/path/to/root/path/to/file.php'

        # SUT
        self._command = CreateFileCommandTestSubclass('sublime dummy', self._plugin_settings)
        self._command.file_creator_instance = FileCreatorSpy()


class CreateFileCommandTestSubclass(CreateFileCommand):
    file_creator_instance = None

    def _get_file_creator(self):
        return self.file_creator_instance


class FileCreatorSpy:
    def __init__(self):
        self.path_to_create = None

    def create(self, path):
        self.path_to_create = path


class PluginSettingsStub:
    pass


class ViewStub:
    def __init__(self):
        self.project_folders = None

    def window(self):
        window = WindowStub()
        window.folders = lambda: self.project_folders

        return window


class WindowStub:
    def folders(self):
        pass
