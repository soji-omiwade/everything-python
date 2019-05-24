import unittest

class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertRaises(ValueError, int, 'xyz')
    def test_regex(self):
        p = r"invalid literal for int\(\) with base 10: '...'"
        e = ValueError
        self.assertRaisesRegex(e, p, int, 'xyz')
    def test2(self):
        with(self.assertRaises(ValueError)) as cm:
            int('xyz')
if __name__ == '__main__':
    unittest.main()