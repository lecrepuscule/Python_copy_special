import unittest
import copyspecial

class TestCopySpecialFunctions(unittest.TestCase):
  def test_get_special_paths(self):
    self.assertEqual(copyspecial.get_special_paths("."), 
    [
      '/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecialxyz__hello__.txt', '/Users/Cloud/Documents/IT Course/Python/Google for Education/google-python-exercises/copyspecialzz__something__.jpg'
    ])

if __name__ == '__main__':
    unittest.main()