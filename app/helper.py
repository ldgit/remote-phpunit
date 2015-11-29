class Helper:
    def __init__(self, settings, sublime):
        self._plugin_settings = settings
        self._sublime = sublime

    def find_root(self, window):
        if self._plugin_settings.root != '':
            return self._plugin_settings.root

        try:
            return window.folders()[0]
        except IndexError:
            self._sublime.status_message(u"Remote PHPUnit: could not find root folder")
            return ''
