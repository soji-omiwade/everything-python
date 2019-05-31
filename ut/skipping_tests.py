import unittest
import sys
class MyTestCase(unittest.TestCase):

    @unittest.skipIf(False, "just skip the whole class...conditionally")
    def setUp(self):
        pass
        
    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        self.fail("shouldn't happen")
        
    @unittest.skipIf(sys.platform.startswith('win'), "skipping: ain't linux")
    def test_linux(self):
        pass
        
    @unittest.skipUnless(sys.platform.startswith('win'), "won't be skipped")
    def test_windows_support(self):
        pass