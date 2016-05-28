import unittest
from app.remote_phpunit_settings import RemotePHPUnitSettings


class TestRemotePHPUnitSettings(unittest.TestCase):
    def setUp(self):
        self.sublime = SublimeSpy()
        self.settings = RemotePHPUnitSettings(self.sublime)

    def test_correct_settings_file_is_loaded(self):
        self.settings.root
        self._assertThatCorrectSublimeSettingsFileIsLoaded(self.settings, self.sublime.settings_file_to_load)

    def test_get_root(self):
        self.assertEqual(SublimeSettingsStub.ROOT_SETTING, self.settings.root)

    def test_get_cl_options(self):
        self.assertEqual(SublimeSettingsStub.CL_OPTIONS_SETTING, self.settings.cl_options)

    def test_get_path_to_phpunit(self):
        self.assertEqual(SublimeSettingsStub.PATH_TO_PHPUNIT, self.settings.path_to_phpunit)

    def test_get_tests_folder(self):
        self.assertEqual(SublimeSettingsStub.TESTS_FOLDER, self.settings.tests_folder)

    def test_get_xml_config(self):
        self.assertEqual(SublimeSettingsStub.XML_CONFIG, self.settings.xml_config)

    def _assertThatCorrectSublimeSettingsFileIsLoaded(self, settings, sublime_settings_file):
        self.assertEqual(settings._settings_file, sublime_settings_file)


class SublimeSpy:
    def __init__(self):
        self.settings_file_to_load = None

    def load_settings(self, settings_file):
        self.settings_file_to_load = settings_file

        return SublimeSettingsStub()


class SublimeSettingsStub:
    ROOT_SETTING = 'path to root'
    CL_OPTIONS_SETTING = 'a command line option list...'
    PATH_TO_PHPUNIT = 'path to phpunit'
    TESTS_FOLDER = 'path to test folder'
    XML_CONFIG = [{"name": "phpunit.xml", "path": "tests"}]

    def get(self, setting_name):
        if setting_name == 'root':
            return self.ROOT_SETTING

        if setting_name == 'options':
            return self.CL_OPTIONS_SETTING

        if setting_name == 'path_to_phpunit':
            return self.PATH_TO_PHPUNIT

        if setting_name == 'tests_folder':
            return self.TESTS_FOLDER

        if setting_name == 'xml_config':
            return self.XML_CONFIG

        return None
