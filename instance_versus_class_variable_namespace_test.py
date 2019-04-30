import unittest

"""
purpose: when the instance variable gets an assignment, it no longer references the class variable. until that point, it does!
"""

class Logger:
    singleton = []
    @classmethod 

class InstanceVsClassVariableTest(unittest.TestCase):
    def test_namespace_change_on_instance_variable(self):
        l = Logger()
        self.assertIs(l.singleton, Logger.singleton)
        l.singleton.append(42)
        self.assertIs(l.singleton, Logger.singleton)
        l.singleton = []
        self.assertIsNot(l.singleton, Logger.singleton)
   
if __name__ == '__main__':
    unittest.main()

       