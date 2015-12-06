#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import os

import sublime
import sublime_plugin

try:
    # ST 3
    from .app.settings import Settings
    from .app.commands import *
except ValueError:
    # ST 2
    from app.settings import Settings
    from app.commands import *

plugin_settings = Settings(sublime)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        command = PHPUnitCommand(sublime, plugin_settings)
        command.create_run_test_command(self.view)

    def is_enabled(self):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        return command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        command = PHPUnitCommand(sublime, plugin_settings)
        command.create_run_test_on_folder(dirs, self.window)


class OpenTestFile(sublime_plugin.TextCommand):
    def run(self, edit):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        command.open_test_file(self.view.file_name(), self.view.window())

    def is_enabled(self):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        return command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class OpenSourceFile(sublime_plugin.TextCommand):
    def run(self, edit):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        command.open_source_file(self.view.file_name(), self.view.window())

    def is_enabled(self):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        return command.source_file_exists(self.view.file_name())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class CreateTestFile(sublime_plugin.TextCommand):
    def run(self, edit):
        command = CreateFileCommand(sublime, plugin_settings)
        command.create_test_file(self.view)

    def is_enabled(self):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        return not command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())
