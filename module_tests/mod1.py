import sys
from . import mod2

print('start mod2')
print(mod2.foo())
print('end mod2')

print('name: {}\npackage: {}'.format(__name__, __package__))
print('\nargv:')
for x in sys.argv:
    print(x, end=', ')
print()