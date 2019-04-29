import unittest

class DictMergeTestCase(unittest.TestCase):
    def test_1(self):
        x = {'a':1, 'b':2}
        y = {'b':10, 'c': 11}
        xp = x.copy()
        yp = y.copy()
        z = x.update(y)

        self.assertDictEqual(y, yp)
        self.assertDictEqual(x, {'a': 1, 'b': 10, 'c': 11})
        self.assertIsNone(z)
        
        z = {**xp, **y}
        self.assertDictEqual(z, x)
        
        
if __name__ == '__main__':
    unittest.main()

    