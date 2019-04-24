def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
"""
output: test spam, nonlocal spam, nonlocal spam, global spam
very interesting: nonlocal is not local but also not global.
ALSO very interesting: you can define or refer to a global within a function
by simply saying 'global' in front of the corresponding reference!

"""