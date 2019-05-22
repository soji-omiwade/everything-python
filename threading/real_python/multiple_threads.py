import logging
import threading
import time

def thread_function(thread_name, a, b, *c):
    # print(f'thread {threading.current_thread().name}: starts...')
    # print(f'args: {args}')
    print(f'thread {threading.current_thread().name}: {thread_name}, {a}, {b}, {c}')
    time.sleep(.1)
    # print(f'thread {threading.current_thread().name}: ends...')


def locking_thread_function(thread_name, *args):
    def foo(l):
        print('sub-func acquiring l...')
        l.acquire()
        print('sub-func acquired l. sub-func releasing l...')
        l.release()
        print('sub-func released l')
    
    print(args)
    fmt = '%(asctime)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')
    
    print(f'thread {thread_name} starting')
    l = args[0]
    time.sleep(.1)
    l.acquire()
    foo(l)
    time.sleep(.1)
    print(f'thread {thread_name} finishing')
    l.release()

if __name__ == '__main__': 
    fmt = '%(asctime)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')
    
    threads = []
    for index in range(3):
        logging.info('main create and start thread %d', index)
        x = threading.Thread(target=thread_function, args=(index,index**2,'pooh', 'cow',))
        threads.append(x)
        x.start()
        
    for index, thread in enumerate(threads):
        logging.info('main: before joining thread %d', index)
        threads[index].join()
        logging.info('main: thread %d done; %s', index, threads[index].name)
    logging.info('main finishing')
