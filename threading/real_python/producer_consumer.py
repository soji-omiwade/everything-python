import threading
import random
from concurrent.futures import ThreadPoolExecutor
SENTINEL = object()

def producer(pipeline):
    """pretend we are getting a message from the network"""
    for index in range(10):
        message = random.randint(1, 101)
        print('producer got message {} from the network'.format(message))
        pipeline.set_message(message)
        
    #send a sentinel message to tell consumer we are done
    print('setting the SENTINEL!!!')
    pipeline.set_message(SENTINEL)
    
def consumer(pipeline):
    """pretend we are saving a number in the database"""
    message = pipeline.get_message()
    while message is not SENTINEL:
        print('consumer storing message {} to the db'.format(message))
        message = pipeline.get_message()
    print('ALL done')
         
class Pipeline:
    """ class to allow a single element pipeline between producer and consumer
    
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
        
    def get_message(self):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        return message
        
    def set_message(self, message):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()
        
if __name__ == '__main__':
    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
