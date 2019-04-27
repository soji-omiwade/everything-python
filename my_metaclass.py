"""
The code samples in here derive mostly from:
https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
"""
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


print('\n let the metaclass showdown begin!')
"""what are metaclasses!"""
#the metaclass will automatically get passed the same argument
#that you usally pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object with the list of its attribute turned into uppercase
    """

    ##pick up any attribute that doesnt start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val
            
    #let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr

class Foo():
    bar = 'bip'
print('hasattr(Foo, "bar"):', hasattr(Foo, 'bar'))
print('hasattr(Foo, "BAR"):', hasattr(Foo, 'BAR'))

f = Foo()
print('hasattr(f, bar):', hasattr(f, 'bar'))
print('hasattr(f, BAR):', hasattr(f, 'BAR'))

class Zoo(Foo, metaclass = __metaclass__):
    car = 'zoom'
    
print("hasattr(Zoo, 'CAR'):", hasattr(Zoo, 'CAR'))
#above is False until you pass it a metaclass that does the uppercase
print('hasattr(Zoo, "BAR"):', hasattr(Zoo, 'BAR'))
#to above, True/False depending on whether parent has a customized 
#   metaclass 

print('\n meta class creation using object based programming')
#remember type is a class like str and int and hence can be extended
class UpperAttrMetaclass(type):
    def __new__(upper_attr_metaclass, future_class_name, future_class_parents, \
    future_class_attr):
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return type(future_class_name, future_class_parents, uppercase_attr)
class UpperAttrMetaclassTest(metaclass = UpperAttrMetaclass):
    bar = 'bip'
print('hasattr(UpperAttrMetaclassTest, "bar"):', 
    hasattr(UpperAttrMetaclassTest, 'bar'))
print('hasattr(UpperAttrMetaclassTest, "BAR"):', 
    hasattr(UpperAttrMetaclassTest, 'BAR'))

f = UpperAttrMetaclassTest()
print('hasattr(f, bar):', hasattr(f, 'bar'))
print('hasattr(f, BAR):', hasattr(f, 'BAR'))
        

print('\n meta class creation using OOP')
class UpperAttrMetaclassOOP(type):
    def __new__(upper_attr_metaclass, future_class_name, future_class_parents, \
    future_class_attr):
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return type.__new__(upper_attr_metaclass, future_class_name,\
            future_class_parents, uppercase_attr)
        
class UpperAttrMetaclassTestOOP(metaclass = UpperAttrMetaclassOOP):
    bar = 'bip'
print('hasattr(UpperAttrMetaclassTestOOP, "bar"):', 
    hasattr(UpperAttrMetaclassTestOOP, 'bar'))
print('hasattr(UpperAttrMetaclassTestOOP, "BAR"):', 
    hasattr(UpperAttrMetaclassTestOOP, 'BAR'))

f = UpperAttrMetaclassTestOOP()
print('hasattr(f, bar):', hasattr(f, 'bar'))
print('hasattr(f, BAR):', hasattr(f, 'BAR'))


print('\n meta class creation using OOP')
class UpperAttrMetaclassOOPForProduction(type):
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclassOOPForProduction, cls).__new__(\
            cls, clsname, bases, uppercase_attr)

class UpperAttrMetaclassOOPForProductionTest(\
    metaclass = UpperAttrMetaclassOOPForProduction):
    bar = 'bip'
print('hasattr(UpperAttrMetaclassOOPForProductionTest, "bar"):', 
    hasattr(UpperAttrMetaclassOOPForProductionTest, 'bar'))
print('hasattr(UpperAttrMetaclassOOPForProductionTest, "BAR"):', 
    hasattr(UpperAttrMetaclassOOPForProductionTest, 'BAR'))

f = UpperAttrMetaclassOOPForProductionTest()
print('hasattr(f, bar):', hasattr(f, 'bar'))
print('hasattr(f, BAR):', hasattr(f, 'BAR'))
