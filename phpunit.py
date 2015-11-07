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
from app.settings import Settings

plugin_settings = Settings()

# plugin_settings.cl_options
# plugin_settings.path_to_phpunit
# print(plugin_settings.root)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        root_folder = Root.find(plugin_settings, self.view.window())
        file_path = self.view.file_name()

        print(root_folder)
        print(file_path)
        # sublime.set_clipboard(str(self.window.folders()))
        # print(dir(self.window.active_view()))


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        root_folder = Root.find(plugin_settings, self.window)
        folder_path = dirs[0]
        print(root_folder)
        print(folder_path)


class Root():
    @staticmethod
    def find(settings, window):
        if settings.root != '':
            return settings.root

        try:
            return window.folders()[0];
        except IndexError:
            sublime.error_message(u"Neuspješno dohvaćanje root foldera")
            return ''
