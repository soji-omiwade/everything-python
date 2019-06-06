def make_divide_smart(foo):
    '''
    changing method name to showcase make_divide_smart is just
    a function
    '''
    print('start mds:', foo)
    def smart_divide(a, b):
        print('start smart divide', a, b)
        if b == 0:
            raise ZeroDivisionError('cant divide by zero!')
        else:
            return foo(a,b)
        print('end smart divide')
    print('end mds:', smart_divide)
    return smart_divide
    
    
@make_divide_smart
def divide(a, b):
    print('start divide')
    return a/b;
 
"""
above boils down to 
divide = make_divide_smart(divide)
"""
  
if __name__ == "__main__":
    print(divide(42,2))
    print(divide(24,0))

