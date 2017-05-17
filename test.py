import unittest
import copyspecial
import os

class TestCopySpecialFunctions(unittest.TestCase):
  def test_get_special_paths(self):
    self.assertEqual(copyspecial.get_special_paths("."),
    [
      "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/xyz__hello__.txt",
      "/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecial/zz__something__.jpg"
    ])

if __name__ == '__main__':
    unittest.main()