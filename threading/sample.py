import threading, zipfile
import datetime
from time import sleep

class MultiFileWriting(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            with open('a.txt', 'a') as f:
                f.write(f'spawn: {str(datetime.datetime.now().time())}')
            sleep(1)



spawn = MultiFileWriting()
spawn.start()
print('the main program continues to run in foreground.')

for i in range(1):
    with open('a.txt', 'a') as f:
        f.write(f'main: {str(datetime.datetime.now().time())}')
    sleep(1)

spawn.join(5) #wait for the spawn task to finish
print('main program waited until 5 secs spawn was done')