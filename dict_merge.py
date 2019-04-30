import unittest

"""purpose: showcase how to merge two dictionaries with {} and ** """

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
        #result of above is that x has been overriten, 
        #and has the expected final result that should've been in z. and z
        #the variable that should have the final result is None!
        
        z = {**xp, **y}
        self.assertDictEqual(z, x)
        #voila!
        
if __name__ == '__main__':
    unittest.main()

    