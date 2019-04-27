#reversing a list with the yield to create a generator object
def f(l):
    for i in range(len(l)):
        yield l[len(l)-i-1]
        
l = [3, 'm', 43, 21]


"""
a is a generator object from the function f
"""
a = f(l)
for i in a:
    print(i)