class PathBuilder():
    def build(self, filepath, root, tests):
        """
        Takes full filepath, root folder path, and relative unit tests folder path and returns a path to
        corresponding test file.

        :param string filepath: full path, including the filename, of the tested file
        :param string root: root folder of the project
        :param string tests: path to unit test folder, relative to root
        :return:
        """

        filepath = filepath.replace('\\', '/')
        root = root.replace('\\', '/')
        tests = tests.replace('\\', '/')

        filepath = filepath.replace(root + '/', '')

        if not tests.endswith('/'):
            tests += '/'

        final_path = tests + filepath[:-4] + 'Test' + filepath[-4:]

        return final_path[1:] if final_path.startswith('/') else final_path
