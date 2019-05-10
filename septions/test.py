import builtins
from pretty_print import next_sample as ns

class Foo(BaseException):
    pass
# while True:
    # try:
        # x = int(input('Please enter a number: '))
        # raise(Foo())
        # break
    # except ValueError:
        # print('oops! that was no valid number. try again...')
    # except EOFError:
        # print('end of the file! or control z error')
    # except Foo:
        # print('this aint gonna work unless Foo extends BaseException')
        
ns('grouping exceptions in one except clause')
try:
    a = 2 + '2'
    b = spam + 3
except(RuntimeError, TypeError, NameError): 
    print('one of: (RuntimeError, TypeError, NameError)')
    
ns('exceptions that are of BaseException, but not of Exception')

# raise Exception
outside = """
type_check = type(eval(x)) == type
is_base_exception_class = type_check and issubclass(eval(x), BaseException)
is_not_exception_class = type_check and not issubclass(eval(x), Exception)
"""
for x in dir(builtins):
    exec(outside)
    if type_check and is_base_exception_class and is_not_exception_class:
        print(x)
"""result of above: 
...
BaseException
GeneratorExit
KeyboardInterrupt
SystemExit
"""