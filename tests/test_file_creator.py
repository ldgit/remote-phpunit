import unittest
import os
import shutil


class FileCreator:
    def create(self, filepath):
        open(filepath, 'a').close()


class TestFileCreator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.path.realpath(__file__.replace('\\', '/'))
        cls.currentDir = os.path.dirname(path)
        cls.existing_file = os.path.join(cls.currentDir, 'existing_file.php')
        with open(cls.existing_file, 'w') as file:
            file.write('some text')

        cls.new_file = os.path.join(cls.currentDir, 'test_file.php')

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.existing_file)

    def setUp(self):
        self.new_dir_tree = os.path.join(self.currentDir, 'new_folder', 'second_folder')
        self.new_dir = os.path.join(self.currentDir, 'new_folder')
        self.new_file_in_dir_tree = os.path.join(self.currentDir, 'new_folder', 'second_folder', 'testfile.php')
        self.assertFalse(os.path.isfile(self.new_file), 'Guard assertion: file should not already exist')

        # SUT
        self.file_creator = FileCreator()

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

    def test_folder_creation_and_deletion(self):
        # not yet implemented
        os.makedirs(self.new_dir_tree)
        open(self.new_file_in_dir_tree, 'a').close()

        shutil.rmtree(self.new_dir)
