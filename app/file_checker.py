class FileChecker:
    def is_php_file(self, filepath):
        """
        :param string filepath:
        :return: boolean
        """

        return filepath.lower().endswith('.php')
