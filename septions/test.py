import builtins
from pretty_print import next_sample as ns
import sys
class Foo(Exception):
    pass
while True:
    try:
        x = int(input('Please enter a number: '))
        raise Foo
        break
    except ValueError:
        print('oops! that was no valid number. try again...')
    except EOFError:
        print('end of the file! or control z error')
    except Foo:
        print('this will not go into the catch unless Foo is of type Exception')
        break
               
ns('grouping exceptions in one except clause')
try: 
    try:
        a = 2 + '2'
        b = spam + 3
    except(RuntimeError, TypeError, NameError) as e_inst: 
        print('one of: (RuntimeError, TypeError, NameError) occurred')
        assert isinstance(e_inst, TypeError)
        raise NameError
    except NameError:
        print('this will never happen!!')
        sys.exit()
except Exception as e_inst:
    assert(isinstance(e_inst, NameError))
    print(f'catching explicitly raised exception {e_inst}')
    
    
    
    
ns('exceptions that are of BaseException, but not of Exception')
# raise Exception
outside = """
is_class_type = type(eval(x)) == type
is_base_exception_class = is_class_type and issubclass(eval(x), BaseException)
is_not_exception_class = is_class_type and not issubclass(eval(x), Exception)
"""
for x in dir(builtins):
    exec(outside)
    if is_class_type and is_base_exception_class and is_not_exception_class:
        print(x)
"""result of above: 
...
BaseException
GeneratorExit
KeyboardInterrupt
SystemExit
"""