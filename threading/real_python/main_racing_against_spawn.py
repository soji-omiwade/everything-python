import threading as t
import time
import multiple_threads as mt
from importlib import reload as rl
rl(mt)

print('main starts...')
l = t.RLock()
y = t.Thread(target=mt.thread_function, args=('barn', l))
y.start()
# time.sleep(.1)
print('main: waiting to acquire..')
l.acquire()
print('main: acquired.')
l.release()
print('main finishes')