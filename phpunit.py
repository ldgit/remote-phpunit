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

try:
    # ST 3
    from .app.settings import Settings
    from .app.path_builder import PathBuilder
except ValueError:
    # ST 2
    from app.settings import Settings
    from app.path_builder import PathBuilder

plugin_settings = Settings()


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path_builder = PathBuilder()
        file_path = self.view.file_name()
        root_folder = Root.find(plugin_settings, self.view.window())
        tests_folder = 'tests/unit' if plugin_settings.tests_folder == '' else plugin_settings.tests_folder

        test_path = path_builder.build(file_path, root_folder, tests_folder)
        command = plugin_settings.path_to_phpunit + ' ' + ' '.join(plugin_settings.cl_options) + ' ' + test_path

        sublime.set_clipboard(command)


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        root_folder = Root.find(plugin_settings, self.window)
        folder_path = dirs[0]
        print(root_folder)
        print(folder_path)


class Root:
    @staticmethod
    def find(settings, window):
        if settings.root != '':
            return settings.root

        try:
            return window.folders()[0];
        except IndexError:
            sublime.error_message(u"Neuspješno dohvaćanje root foldera")
            return ''
