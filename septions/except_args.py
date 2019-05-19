import sys
import unittest

def foo(a, b):
    raise NameError(a, b)
def goo(p):
    if p == 1:
        raise TypeError
    else:
        int('11.5')
class ExceptionInstanceArgsTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(NameError) as cm:
            foo('spam', 'eggs')
            self.assertTrue(False)    # <---  DOES NOTHING!!
        self.assertTrue(True)    # <---  THIS WILL FAIL, if the arg is False!!
        """
        so if you want to do any self.assert methods with the context manager,
        you have to do it outside the with statement!!!
        """
        self.assertEqual(cm.exception.args, ('spam', 'eggs'))
        
    def test_unittest_assertRaises(self):
        self.assertRaises(NameError, foo, 'pooh', 'barn')
        
    def test_tuple_set(self):
        t = (TypeError, ValueError)
        with self.assertRaises(t) as cm:
            goo(1)
        self.assertTrue(isinstance(cm.exception, TypeError))
        self.assertFalse(isinstance(cm.exception, ValueError)) 
        
        with self.assertRaises(t) as cm:
            goo(0)
        self.assertTrue(isinstance(cm.exception, ValueError))
        self.assertFalse(isinstance(cm.exception, TypeError))         
        
if __name__ == '__main__':
    unittest.main()