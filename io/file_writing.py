import unittest

class MyTestCase(unittest.TestCase):
    def test(self):
        with open(tuple_file) as f:
            s = f.read()
            self.assertEqual(repr_s, s)            

if(__name__ == '__main__'):
    try: del f
    except Exception: print('f doesnt exist')
    else: print('huh: it did exist')

    tuple_file = r'C:\Users\ooo654\everything-python\io\tuple.out'
    with open(tuple_file, 'w') as f:
        value = ('ans', 42)
        repr_s = repr(value)
        f.write(repr_s)
    try: print(f)
    except NameError: print('f doesnt exist as it shouldnt!')
    else: print('huh: expected NameError but i guess with doesnt work that way')
    unittest.main()