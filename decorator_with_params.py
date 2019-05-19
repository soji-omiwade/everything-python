def make_divide_smart(divide):
    def smart_divide(a, b):
        if b == 0:
            raise ZeroDivisionError('cant divide by zero!')
        else:
            return divide(a,b)
    return smart_divide
    
    
@make_divide_smart
def divide(a, b):
    return a/b;
 
"""
above boils down to 
divide = make_divide_smart(divide)
""" 
  
print(divide(42,2))
print(divide(24,0))

