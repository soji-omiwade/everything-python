print('running module', __name__)
def samba(*args):
    pass
def echofilter(*args, **kwargs):
    for i, a in enumerate(args):
        print(i, a)
    for i, a in enumerate(kwargs):
        print(i, a, kwargs[a])