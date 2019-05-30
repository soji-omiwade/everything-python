import unittest

print(f'{__name__}, {__package__}: initializing the module!') 
from .. import forty_two


class DiscoverTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(forty_two, '42')