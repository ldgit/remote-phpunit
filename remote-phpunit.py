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

plugin_settings = Settings(sublime)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path_builder = PathBuilder()
        file_path = self.view.file_name()
        root_folder = Helper.find_root(plugin_settings, self.view.window())

        test_path = path_builder.build(file_path, root_folder, plugin_settings.tests_folder)
        command = plugin_settings.path_to_phpunit + ' ' + ' '.join(plugin_settings.cl_options) + ' ' + test_path

        sublime.set_clipboard(command)


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        path_builder = PathBuilder()
        root_folder = Helper.find_root(plugin_settings, self.window)
        file_path = dirs[0]

        test_path = path_builder.build(file_path, root_folder, plugin_settings.tests_folder)
        command = plugin_settings.path_to_phpunit + ' ' + ' '.join(plugin_settings.cl_options) + ' ' + test_path

        sublime.set_clipboard(command)


class Helper:
    @staticmethod
    def find_root(settings, window):
        if settings.root != '':
            return settings.root

        try:
            return window.folders()[0];
        except IndexError:
            sublime.error_message(u"Neuspješno dohvaćanje root foldera")
            return ''
