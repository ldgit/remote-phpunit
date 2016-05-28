class PathBuilder():
    def build(self, filepath, root, path_to_tests):
        """
        Takes full filepath, root folder path, and relative tests folder path and returns a path to corresponding test
        file.

        :param string filepath: full path, including the filename, of the tested file. Can also be a test file itself.
        :param string root: root folder of the project
        :param string path_to_tests: path to test folder, relative to root
        :return: string path to test file
        """

        filepath, root, path_to_tests = self._replace_backslashes_with_forward_slashes(filepath, root, path_to_tests)
        filepath = self._remove_root_from_filepath(filepath, root)
        path_to_tests = self._add_trailing_slash_if_missing(path_to_tests)
        if not self._file_is_in_test_folder(filepath, path_to_tests):
            path_to_tests = self._add_unit_subfolder_if_missing(path_to_tests)

        return self._build_path(filepath, path_to_tests)

    def _build_path(self, filepath, tests):
        if self._add_trailing_slash_if_missing(filepath).startswith(tests):
            return filepath

        if self._is_php_file(filepath):
            path = tests + self._append_test_suffix(filepath)
        else:
            path = tests + filepath

        return path[1:] if path.startswith('/') else path

    def _add_trailing_slash_if_missing(self, path):
        if not path.endswith('/'):
            path += '/'

        return path

    def _add_unit_subfolder_if_missing(self, tests_path):
        test_path_not_empty = tests_path != '/'
        if test_path_not_empty and not tests_path.endswith('unit/'):
            tests_path += 'unit/'

        return tests_path

    def _remove_root_from_filepath(self, filepath, root):
        return filepath.replace(self._add_trailing_slash_if_missing(root), '')

    def _replace_backslashes_with_forward_slashes(self, filepath, root, tests):
        filepath = filepath.replace('\\', '/')
        root = root.replace('\\', '/')
        tests = tests.replace('\\', '/')

        return filepath, root, tests

    def _append_test_suffix(self, filepath):
        return filepath[:-4] + 'Test' + filepath[-4:]

    def _is_php_file(self, filepath):
        return filepath[-4:] == '.php'

    def _file_is_in_test_folder(self, filepath, path_to_tests):
        if filepath.startswith(path_to_tests):
            return True

        return False
