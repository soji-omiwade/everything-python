import unittest

# print(f'package "{__package__}" and type: "{type(__package__)}"')
# print('name:', __name__)
# from unit_testing import a
print(f'{__name__}, {__package__}: initializing the module!') 

# from .. import a
class MyTestCase(unittest.TestCase):
    # def setUp(self):
        # raise AssertionError
    def test(self):
        s = 'hello world'
        self.assertRaises(TypeError, s.split, 2)
        
    def test_global_import_from_module_init(self):
        self.assertEqual(42, 42)
        

class MyOtherTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1.0)
"""
when you run the unittest as a module, you don't need the if below!
"""
# if __name__ == '__main__':
    # unittest.main()