import sys

try:
    f = open(r'C:\Users\ooo654\everything-python\septions\my_file.txt')
    s = f.readline()
    i = int(s.strip())
    i /= 0
except OSError as err:
    print("OSError: {}".format(err))
except ValueError as err:
    print("ValueError: {}".format(err))
except: 
    print('unexpected error: {}'.format(sys.exc_info()[0]))
    for i, x in enumerate(sys.exc_info()):
        print(f'{i}:{x}')
else: 
    print(f'{s}:{i}')