from .path_builder import PathBuilder


class PHPUnitCommand:
    def __init__(self, sublime, plugin_settings):
        self._sublime = sublime
        self._plugin_settings = plugin_settings

    def create_run_test_command(self, view):
        path_builder = PathBuilder()
        file_path = view.file_name()
        root_folder = self.find_root(view)

        test_path = path_builder.build(file_path, root_folder, self._plugin_settings.tests_folder)

        command = self._plugin_settings.path_to_phpunit + ' ' + ' '.join(self._plugin_settings.cl_options) + ' ' \
                  + test_path

        self._sublime.set_clipboard(command.replace('  ', ' '))

    def find_root(self, view):
        if self._plugin_settings.root != '':
            return self._plugin_settings.root

        try:
            return view.window().folders()[0];
        except IndexError:
            self._sublime.error_message(u"Neuspjesno dohvacanje root foldera")
            return ''
