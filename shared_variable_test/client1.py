import logger
import unittest

def use_logger():
    return logger.Logger.get_instance()
    
class create_singleton_logger_instance_test(unittest.TestCase):
    def test(self):
        self.assertIs(use_logger(), use_logger())
if __name__ == '__main__':
    unittest.main()