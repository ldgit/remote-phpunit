from .path_builder import PathBuilder


class PHPUnitCommand:
    def __init__(self, sublime, plugin_settings):
        self._sublime = sublime
        self._plugin_settings = plugin_settings

    def create_run_test_command(self, view):
        file_path = view.file_name()
        root_folder = self._find_root(view.window())

        test_path = self._get_path_builder().build(file_path, root_folder, self._plugin_settings.tests_folder)
        command = self._build_command(test_path)

        self._sublime.set_clipboard(command.replace('  ', ' '))

    def create_run_test_on_folder(self, dirs, window):
        root_folder = self._find_root(window)
        file_path = dirs[0]

        test_path = self._get_path_builder().build(file_path, root_folder, self._plugin_settings.tests_folder)
        command = self._build_command(test_path)

        self._sublime.set_clipboard(command.replace('  ', ' '))

    def _build_command(self, test_path):
        return self._plugin_settings.path_to_phpunit + ' ' + ' '.join(self._plugin_settings.cl_options) + ' ' \
                  + test_path

    def _find_root(self, window):
        if self._plugin_settings.root != '':
            return self._plugin_settings.root

        try:
            return window.folders()[0];
        except IndexError:
            self._sublime.error_message(u"Neuspjesno dohvacanje root foldera")
            return ''

    def _get_path_builder(self):
        return PathBuilder()
