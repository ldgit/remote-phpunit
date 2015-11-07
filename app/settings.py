import sublime, sublime_plugin


class Settings():
    _settings_file = 'PHPUnit.sublime-settings'

    @property
    def root(self):
        return self._get('root')

    @property
    def cl_options(self):
        return self._get('options')

    @property
    def path_to_phpunit(self):
        return self._get('path_to_phpunit')

    @classmethod
    def _get(cls, name):
        settings = sublime.load_settings(cls._settings_file)

        return settings.get(name)
