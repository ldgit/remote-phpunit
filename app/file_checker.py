class FileChecker:
    def is_php_file(self, filepath):
        """
        :param string filepath:
        :return: boolean
        """
        if filepath is None:
            return False

        return filepath.lower().endswith('.php')
