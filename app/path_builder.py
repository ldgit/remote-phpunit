class PathBuilder():
    def build(self, filepath, root, tests):
        """
        Takes full filepath, root folder path, and relative unit tests folder path and returns a path to
        corresponding test file.

        :param string filepath: full path, including the filename, of the tested file
        :param string root: root folder of the project
        :param string tests: path to unit test folder, relative to root
        :return: string path to test file
        """

        filepath, root, tests = self._replace_backslashes_with_forward_slashes(filepath, root, tests)
        filepath = self._remove_root_from_filepath(filepath, root)
        tests = self._add_trailing_slash_if_missing(tests)

        return self._build_path(filepath, tests)

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
