import unittest
import client1

"""
purpose: show that the logger module is not reimported to create a new logger
"""
class GetInstanceTest(unittest.TestCase):
    def test_(self):
            logger_for_first_client = client1.c1logger()

            import logger as shoe
            logger_for_second_client = shoe.Logger.get_instance()

            self.assertIs(logger_for_second_client, logger_for_first_client)

if __name__ == '__main__':
    unittest.main()
