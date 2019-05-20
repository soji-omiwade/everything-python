import unittest
class Error(Exception):
    """Base class for exceptions in this module."""
    pass
    
class InputError(Error):
    """Exception raised for errors in the input
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class TransitionError(Error):
    error_message = 'cant leave your state. boring automata'
    """Raised when an operation attempts a state transition that's not allowed
    
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
        
        
def foo(bar = True):
    if bar:
        raise InputError('42 = x', 'cant assign to literal')
    
def goo():
    raise TransitionError(0, 1, TransitionError.error_message)
    
class UserDefinedExceptionsTestCase(unittest.TestCase):

    def test(self):
        self.assertRaises(InputError, foo)
        
    def test2(self):
        with self.assertRaises(TransitionError) as cm:
            goo()
        self.assertEqual(cm.exception.message, TransitionError.error_message)
        
if __name__ == '__main__':
    unittest.main()