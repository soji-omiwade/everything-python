"""
showcased that the from throws in what's in the module (i.e., 
the module package. if not found then it looks to see if there's a module in the package with that name)

lets get more specific:  

output  when __all__ is not used: 
>>> from sound.effects import *
initializing the sound package
initializing the effects sub-package
echo echo echo echo
>>> dir()
['TestClass', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'test_method']


now output when it is used: everythin
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> from sound.effects import *
initializing the sound package
initializing the effects sub-package
echo echo echo echo

so here's what happens

if __all__ is not defined, load the names in the __init__ module of the package
and load no modules.
if __all__ is defined, load only the names (including any module specified) there
"""


print('initializing the effects sub-package')
a = 'effects'
class TestClass:
    pass
def test_method():
    pass

__all__ = ['echo']
