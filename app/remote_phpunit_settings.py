class RemotePHPUnitSettings:
    PLUGIN_FOLDER = 'remote-phpunit'

    def __init__(self, sublime):
        self._settings_file = self.PLUGIN_FOLDER + '.sublime-settings'
        self._sublime = sublime

    @property
    def root(self):
        return self._get('root')

    @property
    def cl_options(self):
        return self._get('options')

    @property
    def path_to_phpunit(self):
        return self._get('path_to_phpunit')

    @property
    def tests_folder(self):
        return self._get('tests_folder')

    @property
    def xml_config(self):
        return self._get('xml_config')

    def _get(self, name):
        settings = self._sublime.load_settings(self._settings_file)

        return settings.get(name)
