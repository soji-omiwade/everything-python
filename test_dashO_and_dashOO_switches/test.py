"""is this the module's doc_string?

maybe.
"""
a = 42
assert a == 42
b = 12349712347892
b -= a
"""
this is not part of the doc of course
"""
b -= a
b += 1
b -= 1
b += 2 * a
assert b == 12349712347892
assert b is not 12349712347892
print('alld done!')

def f():
    """this function does nothing

    No, really, it doesn't do anything.

    https://docs.python.org/3/tutorial/modules.html#compiled-python-files
    Some tips for experts:

    You can use the -O or -OO switches on the Python command to reduce the size of a compiled module. The -O switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings. Since some programs may rely on having these available, you should only use this option if you know what you’re doing. “Optimized” modules have an opt- tag and are usually smaller. Future releases may change the effects of optimization.
    A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; the only thing that’s faster about .pyc files is the speed with which they are loaded.
    The module compileall can create .pyc files for all modules in a directory.
    There is more detail on this process, including a flow chart of the decisions, in PEP 3147.
    """
    pass