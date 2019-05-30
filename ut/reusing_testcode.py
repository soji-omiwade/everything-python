import unittest

def testSomething():
    l = [2,3,4]
    assert len(l) is 3
    
testcase = unittest.FunctionTestCase(testSomething,)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(testcase)
    return suite
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())