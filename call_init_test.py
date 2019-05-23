class TypeTest(type):
    def __call__(cls, *args, **kwargs):
        print(f'call start: {cls}--{args}--{kwargs}')
        inst = super().__call__(*args, **kwargs)
        print(f'call end')
        return inst
       
    def __new__(*args, **kwargs):
        print(f'new start: {args}--{kwargs}')
        new_val =  type.__new__(*args, **kwargs)
        print(f'new end')
        return new_val
        
class Foo(metaclass=TypeTest):
    def __init__(self, a, b=42, *args, **kwargs):
        print(f'init-{self}--{a}--{b}--{args}--{kwargs}')
        
f = Foo(42, 43, 44, 45, fish=3, camel = 'em')