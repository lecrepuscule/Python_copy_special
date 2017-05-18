import unittest
import copyspecial
import os
import commands

class TestGetSpecialPaths(unittest.TestCase):
  def test_get_special_paths(self):
    test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/"
    self.assertEqual(copyspecial.get_special_paths("."),
    [
      test_path + "xyz__hello__.txt",
      test_path + "zz__something__.jpg"
    ])

class TestCopyToPath(unittest.TestCase):

  def setUp(self):
    self.test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/tmp/"

  def create_test_path(self):
    os.mkdir(self.test_path)

  def remove_test_path(self):
    cmd = "rm -r '" + self.test_path + "'"
    commands.getstatusoutput(cmd)

  def test_copy_to_non_existing_path(self):
    self.remove_test_path()
    self.assertFalse(os.path.exists(self.test_path))
    copyspecial.copy_to(copyspecial.get_special_paths("."), "./tmp")
    self.assertEqual(copyspecial.get_special_paths(self.test_path), 
    [
      self.test_path + "xyz__hello__.txt",
      self.test_path + "zz__something__.jpg"
    ])
    self.remove_test_path()

  def test_copy_to_existing_path(self):
    self.create_test_path()
    self.assertTrue(os.path.exists(self.test_path))
    copyspecial.copy_to(copyspecial.get_special_paths("."), "./tmp")
    self.assertEqual(copyspecial.get_special_paths(self.test_path), 
    [
      self.test_path + "xyz__hello__.txt",
      self.test_path + "zz__something__.jpg"
    ])
    self.remove_test_path()

class TestZipToPath(unittest.TestCase):
  def setUp(self):
    self.test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/tmp.zip"
    self.remove_test_path()

  def tearDown(self):
    self.remove_test_path()

  def remove_test_path(self):
    cmd = "rm -r '" + self.test_path + "'"
    commands.getstatusoutput(cmd)

  def test_zip_to_existing_path(self):
    self.assertFalse(os.path.exists(self.test_path))
    copyspecial.zip_to(copyspecial.get_special_paths("."), "tmp.zip")
    self.assertTrue(os.path.exists(self.test_path))

  def test_zip_to_non_existing_path(self):
    self.assertFalse(os.path.exists(self.test_path))
    with self.assertRaises(Exception) as context: copyspecial.zip_to(copyspecial.get_special_paths("."), "noway/tmp.zip")
    self.assertTrue('zip I/O error: No such file or directory' in str(context.exception))

if __name__ == '__main__':
    unittest.main()