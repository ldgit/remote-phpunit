from ..file_checker import FileChecker
from ..path_builder import PathBuilder
from ..helper import Helper
from ..sublime_facade import SublimeFacade


class PHPUnitCommand:
    def __init__(self, sublime, plugin_settings):
        self._sublime = sublime
        self._plugin_settings = plugin_settings
        self._helper = Helper(self._plugin_settings, self._sublime)
        self._sublime_facade = SublimeFacade()

    def create_run_test_command(self, view):
        self._sublime.set_clipboard(self._get_run_test_command(view))

    def create_run_filtered_test_command(self, view):
        self._sublime.set_clipboard(self._get_run_test_command(view) + ' --filter '
                                    + self._sublime_facade.get_word_at_caret(view))

    def create_run_test_on_folder(self, dirs, window):
        root_folder = self._helper.find_root(window)
        file_path = dirs[0]

        test_path = self._get_path_builder().build(file_path, root_folder, self._plugin_settings.tests_folder)
        command = self._build_command(test_path)

        self._sublime.set_clipboard(command.replace('  ', ' '))

    def is_current_line_php_test_function(self, view):
        line = self._sublime_facade.get_line_at_caret(view)

        return FileChecker().is_php_test_file(view.file_name()) and self._line_is_function_definition(line)

    def _get_run_test_command(self, view):
        file_path = view.file_name()
        root_folder = self._helper.find_root(view.window())
        if root_folder == '':
            return

        test_path = self._get_path_builder().build(file_path, root_folder, self._plugin_settings.tests_folder)
        command = self._build_command(test_path)

        return command.replace('  ', ' ')

    def _build_command(self, test_path):
        if self._plugin_settings.xml_config:
            config_file_option = self._find_most_appropriate_config_by_test_path(test_path)
        else:
            config_file_option = ' -c phpunit.xml '

        return self._plugin_settings.path_to_phpunit + config_file_option + ' '.join(
            self._plugin_settings.cl_options) + ' ' \
               + test_path

    def _find_most_appropriate_config_by_test_path(self, test_path):
        for xml_config in self._plugin_settings.xml_config:
            if test_path.startswith(xml_config['path']):
                config_file_option = ' -c ' + xml_config['name'] + ' '

        return config_file_option

    def _get_path_builder(self):
        return PathBuilder()

    def _line_is_function_definition(self, line):
        import re
        return re.search(r'public[ ]+function', line) is not None
