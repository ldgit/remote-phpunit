import os

from app.file_creator import FileCreator
from app.helper import Helper
from app.path_builder import PathBuilder


class CreateFileCommand:
    def __init__(self, sublime, plugin_settings):
        self._sublime = sublime
        self._plugin_settings = plugin_settings
        self._helper = Helper(self._plugin_settings, self._sublime)
        self._path_builder = PathBuilder()

    def create_test_file(self, view):
        root = self._helper.find_root(view.window())
        test_filepath = self._path_builder.build(view.file_name(), root, self._plugin_settings.tests_folder)

        self._get_file_creator().create(os.path.join(root, test_filepath).replace('\\', '/'))

    def _get_file_creator(self):
        return FileCreator()