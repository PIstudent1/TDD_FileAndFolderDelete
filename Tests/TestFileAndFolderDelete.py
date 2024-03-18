import os
import unittest
import tempfile

class TestFileAndFolderDelete(unittest.TestCase):
    def FileAndFolderDeleteTest(self):
        file_folder_delete = FileAndFolderDelete()
        self.assertIsNotNone(file_folder_delete)

