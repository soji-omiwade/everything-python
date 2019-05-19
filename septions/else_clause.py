import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print(f'cannot open {arg}')
    else: 
        print(f'{arg} has {len(f.readlines())} lines')
        f.close()
        
"""
the code in the else clause has the following features: 
1) it is run only if an exception isn't thrown
    --finally won't help since code here is *always run*
    --after the stmts intended to be tried: not good either
        since these codes could be caught by the exception which isn't 
        the intention to start with!
    --outside of the entire try:
        but then you don't know if an exception occured or not!
        since some exceptions will not re-raise.
        
        that's it!!!!!!! so it is as it says: the code is executed 
        if nothing in the try raised any of the specified handlers, 
        and is guaranteed not to be squashed by an except in the try!!!!
"""
