import os


class FileCreator:
    def create(self, filepath):
        try:
            open(filepath, 'a').close()
        except IOError:
            directory_path = os.path.dirname(filepath)
            os.makedirs(directory_path)
            open(filepath, 'a').close()