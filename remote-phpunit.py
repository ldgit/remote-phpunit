#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import os

import sublime
import sublime_plugin

try:
    # ST 3
    from .app.commands import *
except ValueError:
    # ST 2
    from app.commands import *

plugin_settings = RemotePHPUnitSettings(sublime)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        PHPUnitCommand(sublime, plugin_settings).create_run_test_command(self.view)

    def is_enabled(self):
        command = FileCommand(plugin_settings, os.path, sublime)
        return command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class GetFilteredTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        PHPUnitCommand(sublime, plugin_settings).create_run_filtered_test_command(self.view)

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        PHPUnitCommand(sublime, plugin_settings).create_run_test_on_folder(dirs, self.window)


class OpenTestFile(sublime_plugin.TextCommand):
    def run(self, edit):
        FileCommand(plugin_settings, os.path, sublime).open_test_file(self.view.file_name(), self.view.window())

    def is_enabled(self):
        command = FileCommand(plugin_settings, os.path, sublime)
        return command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class OpenSourceFile(sublime_plugin.TextCommand):
    def run(self, edit):
        FileCommand(plugin_settings, os.path, sublime).open_source_file(self.view.file_name(), self.view.window())

    def is_enabled(self):
        return FileCommand(plugin_settings, os.path, sublime).source_file_exists(self.view.file_name())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())


class CreateTestFile(sublime_plugin.TextCommand):
    def run(self, edit):
        CreateFileCommand(sublime, plugin_settings).create_test_file(self.view)

    def is_enabled(self):
        command = FileCommand(plugin_settings, os.path, sublime)
        return not command.test_file_exists(self.view.file_name(), self.view.window())

    def is_visible(self):
        return FileChecker().is_php_file(self.view.file_name())
