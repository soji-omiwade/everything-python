def scope_test():
    def do_local():
        print('local-print:', spam)
        spam = "local spam"
    def do_nonlocal():
        # kimbo = spam; print('do_nonlocal(): ', spam)
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"        
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print(scope_test.__dict__)
print("In global scope:", spam)

# output: test spam, nonlocal spam, nonlocal spam, global spam
# very interesting: nonlocal is not local but also not global.
# ALSO very interesting: you can define or refer to a global within a function, by simply saying 'global' in front of the corresponding reference!
# testing assignments to an object affect innermost scope
# alright some very interesting stuff: inner scopes can read any of its outers
#   but, note: once you do an assignment, even if it comes before a read of a
#   reference defined outside, you will get compile error. meaning. assignment
#   means 'treat this object as being local' this is only not true when the 
#   object has either nonlocal or global