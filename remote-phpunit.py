#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import sublime
import sublime_plugin
import os

try:
    # ST 3
    from .app.settings import Settings
    from .app.phpunit_command import PHPUnitCommand
    from .app.open_file_command import OpenFileCommand
except ValueError:
    # ST 2
    from app.settings import Settings
    from app.phpunit_command import PHPUnitCommand
    from app.open_file_command import OpenFileCommand

plugin_settings = Settings(sublime)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        command = PHPUnitCommand(sublime, plugin_settings)
        command.create_run_test_command(self.view)


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


class OpenSourceFile(sublime_plugin.TextCommand):
    def run(self, edit):
        command = OpenFileCommand(plugin_settings, os.path, sublime)
        command.open_source_file(self.view.file_name(), self.view.window())

    def is_enabled(self):
        command = OpenFileCommand(plugin_settings, os.path, sublime)

        return command.source_file_exists(self.view.file_name())
