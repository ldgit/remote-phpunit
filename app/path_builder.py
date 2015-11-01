class PathBuilder():
    def __init__(self, root_folder, test_folder):
        if not root_folder or not test_folder:
            raise ValueError()
        self._root = root_folder
        self._tests = test_folder

    def build(self, filepath):
        if not filepath:
            return self._tests + '/'

        root = self._root[:-1] if self._root.endswith('\\') else self._root

        path = self._tests + '/' + filepath.replace(root + '\\', '')

        return path.replace('\\', '/')
