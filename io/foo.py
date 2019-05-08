year = 2016
s = f"""triple-quote print: the 
results___
of
___the {year}
referendum
"""
print(s)
s2 = f'regular quote print: the \
results___\
of\
___the {year}\
referendum\
'
print(s2)

print("\n\n")
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes\n{:2.2%}'.format(yes_votes, percentage))
"""to above: 
-9 means use a buffer of 9 and right justify...i think
"""

print('\n\n')
print("""
#premise: repr(s) is t, such that: print(t) = s. in cpython anyway
#example. 
#s = 'Hello World' --> t = "'Hello World'"
#yeah!
""")


print('\n\nFormatted string literals:')
import math
print(f'pi to 3 decimal places:--{4.8:7.3f}--')

print('\n\npadding:')
d = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for item in d: 
    print('{:10} ==> {:10}'.format(item, d[item]))
    

print('\n\n other modifiers !r !s !a')
animals = 'eels'
pre = 'my hovercraft is full of'
print(pre, f'{animals!r}')
print(pre, f'{animals!s}')
print(pre, f'{animals!a}')
print(pre, repr(f'{animals}'))
print(pre, str(f'{animals}'))
print(pre, ascii(f'{animals}'))

