def make_bike(n, color='black'):
    def bike(arg):
        if arg == 'area':
            from math import pi
            return pi * (n/2)**2
        if arg == 'color':
            return color
    return bike
    
bike8 = make_bike(8) #arg is the diameter of the wheel and color of bike
bike42_red = make_bike(42, 'red')

#operate on a bike as example
print(bike8('area'))
print(bike8('color'))

print(bike42_red('color'))
print(bike42_red('area'))
