import threading
import time
import logging
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        
    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)
        
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)
        
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.getLogger().setLevel(logging.INFO)

    database = FakeDatabase()
    logging.info('testing update. starting value is %d.', database.value)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    #At the end of the with, there is a join to all threads
logging.info('testing update. ending value is %d', database.value)