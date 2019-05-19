import unittest

class Shoe(TypeError): pass

def foo():
    try:
        2 + '2'
    except Shoe:
        print('bad')
    except TypeError:
        raise
        
def goo():
    try:
        2 + '2'
    except Shoe:
        print('bad')
    except TypeError:
        raise Shoe
        
class ExceptionNotRaisedBySubClassTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(TypeError) as err:
            foo()
            self.assertFalse(isinstance(err, Shoe))
    def test2(self):
        with self.assertRaises(TypeError) as err:
            goo()
            self.assertTrue(isinstance(err, Shoe))
if __name__ == '__main__':
    unittest.main()