from pretty_print import next_sample as ns
ns('without default values in named parameters')
def f(c,d, *, a, b, **ka):
    print(c,d, a, b, ka)
f(1,2, b=42, a = '42', e='moo', gg = (2,'2'))

ns('with default values in named parameters')
def f(c,d, *, a=None, b = '42', **ka):
    print(c,d, a, repr(b), ka)
f(1,2, e='moo', gg = (2,'2'))
