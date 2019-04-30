import logger
import unittest

def c1logger():
    return logger.Logger.get_instance()
    
class create_singleton_logger_instance_test(unittest.TestCase):
    def test(self):
        self.assertIs(c1logger(), c1logger())
if __name__ == '__main__':
    unittest.main()