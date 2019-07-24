import unittest
import nose2

class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")



if __name__ == '__main__':
  
  nose2.main()