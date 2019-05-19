import sys
import unittest

def foo():
    try:
        f = open(r'C:\Users\ooo654\everything-python\septions\my_file.txt')
        s = f.readline()
        i = int(s.strip())
        i /= 0
    except OSError as err:
        print("OSError: {}".format(err))
    except ValueError as err:
        print("ValueError: {}".format(err))
    except: 
        for i, x in enumerate(sys.exc_info()):
            print(f'{i}:{x}:{type(x)}')
        raise
    else: 
        print(f'{s}:{i}')
    finally:
        f.close()
    
class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ZeroDivisionError):
            foo()

if __name__ == '__main__':
    unittest.main()
    