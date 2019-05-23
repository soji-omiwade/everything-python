import logging
import threading
import time
from multiple_threads import thread_function
import concurrent.futures

"""
TODO: Ideally, this would be tested  with the unittest framework
"""

if __name__ == '__main__':
    fmt = '%(asctime)s: %(message)s'
    logging.basicConfig(format=fmt, level=logging.INFO, datefmt='%H:%M:%S')

    logging.info('kickoff 3 threads and wait for them to finish...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, ( ('foo-'+str(i), 'cow',) for i in range(3)), 'fish')
    logging.info('all threads done')


