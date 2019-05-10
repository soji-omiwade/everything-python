try: 
    print(__dict__)
except NameError as ne:
    print('error!!!')
print(foo) 
#if you delete foo (assuming somewho it existed before) from the interative 
#screen, the print above will fail, since you are accessing the same namespace!