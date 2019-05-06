import sys
print('running module {0} from package {1}'.format(__name__, __package__))
for x in sys.argv:
    print(x)
def samba(*args):
    pass
def echofilter(*args, **kwargs):
    for i, a in enumerate(args):
        print(i, a)
    for i, a in enumerate(kwargs):
        print(i, a, kwargs[a])