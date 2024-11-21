from app import add,subtract
import unittest

class TestApp(unittest.TestCase):
    def test_add(self):
      return self.assertEqual(add(5,3),8,"Should be 8")
    def test_sub(self):
      return self.assertEqual(subtract(5,3),2,"Should be 2")

if __name__=="__main__":
    unittest.main()
