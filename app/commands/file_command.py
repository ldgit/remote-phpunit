from ..helper import Helper
from ..path_builder import PathBuilder


class FileCommand:
    def __init__(self, plugin_settings, os_path, sublime):
        self._settings = plugin_settings
        self._helper = Helper(self._settings, sublime)
        self._os_path = os_path

    def test_file_exists(self, filepath, window):
        if filepath is None:
            return False

        root = self._helper.find_root(window).rstrip('/')
        test_filepath = self._get_test_filepath(root, filepath)

        return self._os_path.isfile(test_filepath)

    def source_file_exists(self, test_filepath):
        if test_filepath is None:
            return False

        return self._os_path.isfile(self._get_source_filepath(test_filepath))

    def open_test_file(self, filepath, window):
        root = self._helper.find_root(window).rstrip('/')
        test_filepath = self._get_test_filepath(root, filepath)

        window.open_file(test_filepath)

    def open_source_file(self, test_filepath, window):
        window.open_file(self._get_source_filepath(test_filepath))

    def _get_test_filepath(self, root, filepath):
        test_filepath = root + '/' + PathBuilder().build(filepath, root, self._settings.tests_folder)

        return test_filepath.replace('\\', '/')

    def _get_source_filepath(self, test_filepath):
        filepath = test_filepath\
            .replace('\\', '/')\
            .replace(self._settings.tests_folder, '')
        filepath = filepath[:-8] + filepath[-4:]

        return filepath.replace('//', '/')
