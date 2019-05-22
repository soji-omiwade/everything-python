import threading
import time

class Sleeper(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(3600)
        print('Finished background sleeping')

def foo():
    background = Sleeper()
    background.start()
    print('The main program continues to run in foreground.')
    background.join(2)    # Wait for the background task to finish
    print('Main program waited until background was done.')