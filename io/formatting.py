import json
from pretty_print import next_sample as ns

w = 'wishes'; h = 'horses'; b = 'beggars'; r = 'ride'

# s = 'if {first} were {second}, {third} would {fourth}'
# print(s.format(first=w, second=h, third=b, fourth = r))    
    
# b += ' and panhandlers'    
# s = 'if {0} were {1}, {2} would {fourth}'
# print(s.format(w, h, b, fourth = r))

# print('\n\n Using a dictionary: ')
# table = dict(first=w, second=h, third=b, fourth = r)
# s = 'if {0[first]} were {0[second]}, {0[third]} would {0[fourth]}'
# print(s.format(table))


# print('\n\n Using a dictionary with ** notation: ')
# s = 'preface: {}if {first} were {second}, {third} would {fourth}.'
# print(s.format('this is gonna work!\n', **table))


ns('use vars to print all locals via format(**vars())')
for x in vars().copy():
    print(x+':', ('{'+str(x)+'}').format(**vars()))
print()

ns('use vars to print all locals with format(x)')
for x,y in vars().copy().items():
    print(x+':', y)
print()

ns('manual use of vars in format via **vars')
print('w: {w}, h: {h}, b: {b}, r: {r}'.format(**vars()))

ns('manual use of vars in format with normal dict access')
print('w: {0[w]}, h: {0[h]}, b: {0[b]}, r: {0[r]}\n done: {1}'\
.format(vars(), '!!!') )


ns('format with *a and **ka possible?')
a = (w, h, b, r)
table = dict(magic = 42, less_magic = 49)
print('magic{magic} and less-magic:{less_magic}\n{0}-{1}-{4}-{3}'\
.format(*a, 'bar', **table))
print('yes!')

ns('"tidily aligned columns giving integers and the squares and cubes"')
for x in range (1, 11):
    print('{0:2} {1:3} {2:4}'.format(x, x*x, x*x*x))
    
ns('same as above, but with manual string formatting')
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(4))
    
ns("zfill")
print('12'.zfill(5))
print('-3.14'.zfill(5))
print('3.14151234578'.zfill(5))


ns('old string formatting')
import math
print('The value of pi is approx -%5.3f-%3d-' % (math.pi, 42))


ns('simple json serializing and deserializing')
i = 42
s = str(i)
t = (i,s)
l = [x for x in range(i) if x % 10 == 0]
d = {x:x**2 for x in l}
a = (i, s, t, l, d)

with open('json_file', 'w') as f: 
    for x in a:
        json.dump(x, f)
        f.write('\n')