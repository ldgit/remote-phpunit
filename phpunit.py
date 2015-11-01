#!/usr/bin/python
# -*- encoding: UTF-8 -*-

"""
naredba se slaže iz sljedećeg:
root - root radne kopije
test_folder - unit test folder (folder koji oponaša strukturu radne kopije)
console_options - boja, stderr, verbose

Defaults:
root = folder projekta
test folder = tests/unit/


Option file stuff:

FOLDER_SEPARATOR - /
"""

import sublime, sublime_plugin


class Settings:
    @staticmethod
    def get():
        settings_file = 'dl_phpunit.sublime-settings'
        settings = sublime.load_settings(settings_file)
        settings.set("test", 'lalala')
        sublime.save_settings(settings_file)
        print('lala')

Settings.get()

class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # root_folder = self.window.folders()[1];
        try:
            root_folder = self.view.window().folders()[0];
        except IndexError:
            sublime.error_message(u"Neuspješno dohvaćanje root foldera")
            return None

        print(root_folder)
        print(self.view.file_name())


        # sublime.set_clipboard(str(self.window.folders()))
        # print(dir(self.window.active_view()))
