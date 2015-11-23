import unittest
import os
import shutil


class TestFileCreator(unittest.TestCase):
    def setUp(self):
        path = os.path.realpath(__file__.replace('\\', '/'))
        self.currentDir = os.path.dirname(path)
        self.new_file = os.path.join(self.currentDir, 'test_file.php')
        self.new_dir_tree = os.path.join(self.currentDir, 'new_folder', 'second_folder')
        self.new_dir = os.path.join(self.currentDir, 'new_folder')
        self.new_file_in_dir_tree = os.path.join(self.currentDir, 'new_folder', 'second_folder', 'testfile.php')

    def test_file_creation(self):
        open(self.new_file, 'a').close()
        os.remove(self.new_file)

    def test_folder_creation_and_deletion(self):
        os.makedirs(self.new_dir_tree)
        open(self.new_file_in_dir_tree, 'a').close()
        shutil.rmtree(self.new_dir)
