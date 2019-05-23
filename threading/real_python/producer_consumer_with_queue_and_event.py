import queue
import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor

def producer(pipeline, exit_event):
    """pretend we are getting a message from the network"""
    while not exit_event.is_set():
        message = random.randint(1, 101)
        print('producer got message {} from the network'.format(message))
        pipeline.set_message(message)
    print('produce received exit event!')
    
def consumer(pipeline, exit_event):
    """pretend we are saving a number in the database"""
    while not exit_event.is_set() or not pipeline.empty():
        message = pipeline.get_message()
        print_msg = 'consumer storing message {} to the db; len(q) = {}'
        print(print_msg.format(message, pipeline.qsize()))       
    print('ALL done')
         
class Pipeline(queue.Queue):
    """ class to allow a single element pipeline between producer and consumer
    
    """
    def __init__(self):
        super().__init__(maxsize=10)
        
    def get_message(self):
        return self.get()
        
    def set_message(self, message):
        self.put(message)
        
if __name__ == '__main__':
    pipeline = Pipeline()
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(.1)
        print('main about to set event {}'.format(event))
        event.set()
        print('main set it')