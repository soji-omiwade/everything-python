import unittest


def testSomething():
    assert len(l) is 3
    
def foo():
    global l
    l = [2,3,4]
    return l
    
testcase = unittest.FunctionTestCase(testSomething,setUp=foo)

class MyNormalTestCase(unittest.TestCase):
    def test(self):
        pass
def suite():
    suite = unittest.TestSuite()
    suite.addTest(testcase)
    suite.addTest(MyNormalTestCase('test'))
    return suite
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity = 2)
    runner.run(suite())
    # unittest.main()