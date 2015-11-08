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

        filepath, root, tests = self.replace_backslashes_with_forward_slashes(filepath, root, tests)
        filepath = self.remove_root_from_filepath(filepath, root)
        tests = self.add_trailing_slash_if_missing(tests)

        return self.build_path(filepath, tests)

    def build_path(self, filepath, tests):
        if self.is_php_file(filepath):
            path = tests + self.append_test_suffix(filepath)
        else:
            path = tests + filepath

        return path[1:] if path.startswith('/') else path

    def add_trailing_slash_if_missing(self, tests):
        if not tests.endswith('/'):
            tests += '/'

        return tests

    def remove_root_from_filepath(self, filepath, root):
        return filepath.replace(root + '/', '')

    def replace_backslashes_with_forward_slashes(self, filepath, root, tests):
        filepath = filepath.replace('\\', '/')
        root = root.replace('\\', '/')
        tests = tests.replace('\\', '/')

        return filepath, root, tests

    def append_test_suffix(self, filepath):
        return filepath[:-4] + 'Test' + filepath[-4:]

    def is_php_file(self, filepath):
        return filepath[-4:] == '.php'
