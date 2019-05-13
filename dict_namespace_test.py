
try: 
    print(__dict__)
except NameError as ne:
    print('ne: error!!!'.format(ne))
print(__name__)
module_name_test.foo(42)
#if you delete foo (assuming somehow it existed before) from the interative 
#screen, the print above will fail, since you are accessing the same namespace!