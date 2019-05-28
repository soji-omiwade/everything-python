import unittest

class MyTestCase(unittest.TestCase):
    def test(self):
        s = 'hello world'
        self.assertRaises(TypeError, s.split, 2)
        
    def test2(self):
        self.assertTrue(True)
        
"""
when you run the unittest as a module, you don't need the if below!
"""
# if __name__ == '__main__':
    # unittest.main()