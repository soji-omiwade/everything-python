"""
this module shows that we can simulate object oriented programming via closure  functions. 
note how make_bike serves to create a bike with a certain diameter and color. that's like constructing. 
the if statements inside the inner function is really effectively an anonymous function where each if represents a method in normal classes
note how i have to use nonlocal to set the value of n!!!
this allows me to change the state of the "object". pretty cool. all only
with the use of inner functions!!!
"""
def make_bike(n, color='black'):
    def bike(*args):
        nonlocal n
        if args[0] == 'area':
            from math import pi
            return pi * (n/2)**2
        if args[0] == 'color':
            return color
        if args[0] == 'n':
            n = args[1]
    return bike
    
bike8 = make_bike(8) #arg is the diameter of the wheel and color of bike
bike42_red = make_bike(42, 'red')
#operate on a bike as example
print(bike8('area'))
print(bike8('color'))
bike8('n',42)
print(bike8('area'))
print()
print(bike42_red('color'))
print(bike42_red('area'))
