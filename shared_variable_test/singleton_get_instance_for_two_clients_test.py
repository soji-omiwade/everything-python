import unittest
import client1

"""
purpose: show that the logger module is not reimported to create a new logger.
let me be clear: if you reload this module at any time, then you have a new 
instance, from which yes the logger instance will not be the same as any 
instance created before the reload. otherwise, all logger instances will be the
same
"""
class GetInstanceTest(unittest.TestCase):
    def test_(self):
            logger_for_first_client = client1.c1logger()

            import logger as shoe
            logger_for_second_client = shoe.Logger.get_instance()

            self.assertIs(logger_for_second_client, logger_for_first_client)
            
            from importlib import reload as rrr
            rrr(shoe)
            self.assertIs(logger_for_first_client, logger_for_second_client)
            self.assertIsNot(logger_for_first_client, shoe.Logger.get_instance())
            
if __name__ == '__main__':
    unittest.main()
