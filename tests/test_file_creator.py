import os
import shutil
import unittest

from app.file_creator import FileCreator


class TestFileCreator(unittest.TestCase):
    def test_file_creation(self):
        self.file_creator.create(self.new_file)

        self.assertTrue(os.path.isfile(self.new_file), 'File not found in expected path')

        os.remove(self.new_file)

    def test_when_creating_test_file_that_already_exists_do_not_overwrite_it(self):
        self.assertTrue(os.path.isfile(self.existing_file), 'Guard assertion: file must exist before this test starts')

        self.file_creator.create(self.existing_file)

        self.assertTrue(os.path.isfile(self.existing_file), 'File not found in expected path')
        with open(self.existing_file) as readfile:
            self.assertEqual('some text', readfile.read())

    def test_create_file_and_its_directory_tree(self):
        self.file_creator.create(self.new_file_in_new_dir_tree)

        self.assertTrue(os.path.isfile(self.new_file_in_new_dir_tree))

        shutil.rmtree(self.new_dir)

    @classmethod
    def setUpClass(cls):
        path = os.path.realpath(__file__.replace('\\', '/'))
        cls.currentDir = os.path.dirname(path)
        cls.existing_file = os.path.join(cls.currentDir, 'existing_file.php')
        with open(cls.existing_file, 'w') as file:
            file.write('some text')

        cls.new_file = os.path.join(cls.currentDir, 'test_file.php')

        cls.new_dir_tree = os.path.join(cls.currentDir, 'new_folder', 'second_folder')
        cls.new_dir = os.path.join(cls.currentDir, 'new_folder')
        cls.new_file_in_new_dir_tree = os.path.join(cls.currentDir, 'new_folder', 'second_folder', 'testfile.php')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.existing_file)

    def setUp(self):
        self.assertFalse(os.path.isfile(self.new_file), 'Guard assertion: file should not already exist')
        # SUT
        self.file_creator = FileCreator()
