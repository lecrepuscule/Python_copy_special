import unittest
import copyspecial
import os
import commands

class TestCopySpecialFunctions(unittest.TestCase):
  def test_get_special_paths(self):
    test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/"
    self.assertEqual(copyspecial.get_special_paths("."),
    [
      test_path + "xyz__hello__.txt",
      test_path + "zz__something__.jpg"
    ])

  def create_test_path(self, test_path):
    os.mkdir(test_path)

  def remove_test_path(self, test_path):
    cmd = "rm -r '" + test_path + "'"
    commands.getstatusoutput(cmd)

  def test_copy_to_non_existing_path(self):
    test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/tmp/"
    self.remove_test_path(test_path)
    self.assertFalse(os.path.exists(test_path))
    copyspecial.copy_to(copyspecial.get_special_paths("."), "./tmp")
    self.assertEqual(copyspecial.get_special_paths(test_path), 
    [
      test_path + "xyz__hello__.txt",
      test_path + "zz__something__.jpg"
    ])
    self.remove_test_path(test_path)

  def test_copy_to_existing_path(self):
    test_path = "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/tmp/"
    self.create_test_path(test_path)
    self.assertTrue(os.path.exists(test_path))
    copyspecial.copy_to(copyspecial.get_special_paths("."), "./tmp")
    self.assertEqual(copyspecial.get_special_paths(test_path), 
    [
      test_path + "xyz__hello__.txt",
      test_path + "zz__something__.jpg"
    ])
    self.remove_test_path(test_path)

if __name__ == '__main__':
    unittest.main()