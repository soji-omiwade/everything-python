"""classes are objects. everything is an object in python"""
class ObjectCreator(object):
    pass
my_object = ObjectCreator()
print(my_object)

print('\n')
"""classes can be created on the fly"""
def choose_class(name):
    if name == 'foo':
        class Foo:
            pass
        chosen = Foo
    else:
        class Boo:
            pass
        chosen = Boo
    return chosen
print(choose_class('foo'))

print('\n')
"""classes can also be created using type"""
Foo = type('Foo', (), {'bar': True})
print(Foo)
print(Foo.bar)
f = Foo()
print(f)
print(f.bar)
"""and of course inheritance is possible"""
FooChild = type('FooChild', (Foo,), {})
fc = FooChild()
print('child with parent attr', fc.bar)
"""now let's add some methods, the first one, when the class is created"""
print('\n add methods via type')
def echo_bar(self): 
    print(self.bar)
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
print(hasattr(FooChild, 'echo_bar'))
fc = FooChild()
fc.echo_bar()
"""add more methods"""
print('\n add more methods')
fc.bar = False
def echo_bar_more(self):
    print(self.bar)
    print(FooChild.bar)
FooChild.echo_bar_more = echo_bar_more
fc.echo_bar_more()