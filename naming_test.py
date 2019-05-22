from naming import *
import unittest


foo = dir()
    
class PrivateNamesNotLoadedAutomaticallyTestCase(unittest.TestCase):
    def setUp(self):
        self.dir = foo
        
    def test(self):
        self.assertIn('shoe', self.dir)
        self.assertNotIn('_shoe', self.dir)
        self.assertIn('foo', self.dir)
        self.assertNotIn('_foo', self.dir)

if __name__ == '__main__':
    unittest.main()
