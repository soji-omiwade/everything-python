import logging
import threading
import time
from multiple_threads import thread_function
import concurrent.futures

if __name__ == '__main__':
    print(f'thread {threading.current_thread().name}: starts...')

    fmt = '%(asctime)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('kickoff 3 threads and wait for them to finish...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(\
            thread_function\
            , (('foo-'+str(i), 'cow',) for i in range(5))\
            , (x for x in range(4))\
            , 'fis'\
            , 'coo'
            , 'cam'
        )
    logging.info('all threads done')
    print(f'thread {threading.current_thread().name}: ends')
