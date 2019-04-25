def make_divide_smart(divide):
    def smart_divide(a, b):
        if b == 0:
            print('cant divide by zero!')
        else:
            return divide(a,b)
    return smart_divide
@make_divide_smart
def divide(a, b):
    return a/b;
  
print(divide(42,2))
print(divide(24,0))

