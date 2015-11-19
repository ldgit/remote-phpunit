#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import sublime
import sublime_plugin

try:
    # ST 3
    from .app.settings import Settings
    from .app.path_builder import PathBuilder
    from .app.phpunit_command import PHPUnitCommand
except ValueError:
    # ST 2
    from app.settings import Settings
    from app.path_builder import PathBuilder
    from app.phpunit_command import PHPUnitCommand

plugin_settings = Settings(sublime)


class GetTestRunCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        command = PHPUnitCommand(sublime, plugin_settings)
        command.create_run_test_command(self.view)


class GetCommandForFolder(sublime_plugin.WindowCommand):
    def run(self, dirs):
        command = PHPUnitCommand(sublime, plugin_settings)
        command.create_run_test_on_folder(dirs, self.window)
