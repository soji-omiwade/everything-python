import unittest
from test_widget import WidgetTestCase
from test_discover import DiscoverTestCase

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(DiscoverTestCase('test'))
    return suite
    
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())