# from pretty_print import next_sample as ns
import unittest 
"""bare asterisk means: 
    - everything before the asterisk must be non-keyword arg, and
    - everything after must be a keyword arg
    the easiest way to remember this is when you have
    
    def foo(a1, a2, ..., an, *a). from this we know that it is an error
    to have a positional argument after the '*a'. so it's actually pretty
    simple to remember
    
"""
def foo(a, b, *args):
    a1 = a, b
    return args[1:]
    
def foo_kw(a, b, *args, **kwargs):
    a1 = a, b
    return {**{x: x for x in args[1:]}, **kwargs}
     
def foo_kw_bare_asterisk(a, b, *, c = None, **kwargs):
    return (f'{c}, {kwargs}')    

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_foo(self):
        self.assertTupleEqual(foo(1, 2, 3, 4, 5), (4,5))
        
        # with self.assertRaises(TypeError) as cm:
            # foo(1, 2, a = 2, b = 3)
        # self.assertIn('got multiple values for argument', cm.exception.args[0])
        
        # with self.assertRaises(TypeError) as cm:
            # foo(1, 2, x = 3)
        # self.assertIn('got an unexpected keyword argument', cm.exception.args[0])
        
    def test_foo_kw(self):
        a = 1, 2, 3, 4, 5,
        d = dict(spam = '42', eggs = 3)
        value = {4: 4, 5: 5, **d}
        self.assertDictEqual(foo_kw(*a, **d), value)
            
    def test_foo_kw_bare_asterisk(self):
        d = dict(spam = '42', eggs = 3)
        self.assertEqual(foo_kw_bare_asterisk(1,2,c=3, **d), f'3, {repr(d)}')  
        
        
        
        # with self.assertRaises(TypeError) as cm:
            # foo(1, 2, a = 2, b = 3)
        # self.assertIn('got multiple values for argument', cm.exception.args[0])
        
        # with self.assertRaises(TypeError) as cm:
            # foo(1, 2, x = 3)
        # self.assertIn('got an unexpected keyword argument', cm.exception.args[0])
        
    # def test_goo(self):
        # self.assertRaises(TypeError, foo, 1,zx 2, c = 3)
        # pass
        
    # def test_foo_kw(self):
        # self.assertTrue(foo_kw(1, 2, 3, 4, 5))
        # self.assertRaises(TypeError, foo_kw, 1, 2, a = 2, b = 3)
        # self.assertRaises(TypeError, foo_kw, 1, 2, c = 3)

if __name__ == '__main__':
    unittest.main()
    