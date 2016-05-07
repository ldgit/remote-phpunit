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
        filepath = test_filepath
        if test_filepath.startswith('\\\\'):
            separator = '\\'
        else:
            separator = '/'
            filepath = test_filepath.replace('\\', separator)
        filepath = self._remove_tests_folder_from_path(filepath, separator)
        filepath = self._remove_test_suffix_from_filename(filepath)

        return filepath

    def _remove_tests_folder_from_path(self, filepath, folder_separator='/'):
        tests_folder = self._ensure_correct_folder_separator(folder_separator)
        if tests_folder + folder_separator + 'unit' in filepath:
            filepath = filepath.replace(tests_folder + folder_separator + 'unit' + folder_separator, '')
        else:
            filepath = filepath.replace(tests_folder + folder_separator, '', 1)

        return self._ensure_no_double_forward_slashes(filepath)

    def _ensure_no_double_forward_slashes(self, filepath):
        return filepath.replace('//', '/')

    def _ensure_correct_folder_separator(self, folder_separator):
        return self._settings.tests_folder.replace('/', folder_separator).replace('\\', folder_separator)

    def _remove_test_suffix_from_filename(self, filepath):
        return filepath[:-8] + filepath[-4:]
