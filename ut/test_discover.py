import unittest

print(f'{__name__}, {__package__}: initializing the module!') 

class DiscoverTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(True)