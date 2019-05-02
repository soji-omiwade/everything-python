"""to find the fibonacci"""
import unittest

def fibo(n):
    if n in (0,1):
        val = n
    else:
        val = fibo(n-1) + fibo(n-2)
    return val

def fibo2(n):
    a,b = 0,1
    while n >= 2:
        b, a = b + a, b
        print(a,b)
        n -= 1
    return b
class FiboTest(unittest.TestCase):
    def setUp(self):
        self.n = 10
    def test1(self):
        if self.n in (0,1):
            self.assertEqual(fibo(0), 0)
            self.assertEqual(fibo(1), 1)
            self.assertEqual(fibo2(0), 0)
            self.assertEqual(fibo2(1), 1)
            
        else:
            self.assertEqual(fibo(self.n), fibo(self.n-1) + fibo(self.n-2))
            self.assertEqual(fibo(self.n), fibo2(self.n))

    def test2(self):
        self.assertEqual(fibo(4), 3)
        
# if __name__ == '__main__':
    # unittest.main()