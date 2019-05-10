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

print('__builtins__ class: ', __builtins__.__class__)
print(dir(__builtins__))
raise Exception
for x in dir(__builtins__):
    type_check = type(eval(x)) == type
    base_exception_check = issubclass(eval(x), BaseException)
    not_exception_check = not issubclass(eval(x), Exception)
    if type_check and  base_exception_check and not_exception_check:
        print(x)
"""result of above: 
...
BaseException
GeneratorExit
KeyboardInterrupt
SystemExit
"""