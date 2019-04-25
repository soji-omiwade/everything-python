def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)
    return inner
def percent(func):
    def inner(*args, **kwargs):
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30, kwargs['n'])
    return inner   
@star
@percent
def printer(msg, *arguments, **kwargs):
    print(msg, '-', arguments, '-', kwargs)
    
printer('Hello', 1, n = 42)

#this is what the above does
"""
func = decorate_with_percent(func)
func = decorate_with_star(func)
func()
"""