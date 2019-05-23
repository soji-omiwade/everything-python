import unittest

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]
        
        
class SingletonTestCase(unittest.TestCase):
    def setUp(self):
        class Logger(metaclass=Singleton):
            def __init__(self, a):
                pass
        """
        constructor call below does this: Logger.__init__(self, 42)???
        WRONG. eventually init is called. but it is call that calls  iinit . 
        """
        self.l1 = Logger(42) 
        self.l2 = Logger(42)
        self.L = Logger
        
    def test_control(self):
        class ControlLogger:
            def __init__(self):
                pass
        l1 = ControlLogger()
        l2 = ControlLogger()
        self.assertIsNot(l1, l2)
        self.assertTrue(isinstance(l1, ControlLogger)) 
        self.assertTrue(isinstance(l2, ControlLogger))
        
    def test(self):
        self.assertIs(self.l1, self.l2)
        self.assertTrue(isinstance(self.l1, self.L)) 
        self.assertTrue(isinstance(self.l2, self.L))

    def test_basic(self):
        self.assertTrue(issubclass(self.L, object))
        self.assertFalse(issubclass(object, type))
        self.assertTrue(issubclass(type, object))
              
if __name__ == '__main__':
    unittest.main()
