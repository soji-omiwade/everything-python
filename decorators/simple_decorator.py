print('\n\n\n')
class I:
    def __init__(self):
        self.zamba = '42'
    def goo(self):
        return self.zamba + ' goo'
    @property
    def foo(self):
        return 42
def make_ordinary_function_pretty(ordinary_function):
    def pretty_routine():
        ordinary_function()
        print('now i am pretty')
    return pretty_routine
@make_ordinary_function_pretty
def ordinary_funct():
    print('i\'m ordinary')

print('\nnew way using syntactic sugar decorator')
ordinary_funct()

from  time import sleep
sleep(5)

print('\n\nold way')
pretty_funct = make_ordinary_function_pretty(ordinary_funct)
sleep(5)
pretty_funct()


