from .helper import Helper


class OpenFileCommand:
    def __init__(self, plugin_settings, os_path, sublime):
        self._settings = plugin_settings
        self._helper = Helper(self._settings, sublime)
        self._os_path = os_path

    def test_file_exists(self, filepath, window):
        root = self._helper.find_root(window).rstrip('/')
        test_filepath = self._get_test_filepath(root, filepath)

        return self._os_path.isfile(test_filepath)

    def open_test_file(self, filepath, window):
        root = self._helper.find_root(window).rstrip('/')
        test_filepath = self._get_test_filepath(root, filepath)

        window.open_file(test_filepath)

    def _get_test_filepath(self, root, filepath):
        test_filepath = root + '/' + self._settings.tests_folder + self._append_test_suffix(filepath[len(root):])

        return test_filepath.replace('\\', '/')

    def _append_test_suffix(self, filepath):
        return filepath[:-4] + 'Test' + filepath[-4:]
