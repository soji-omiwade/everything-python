from pretty_print import next_sample as ns
import random

print(a)
def print2d(a):
    for r in a:
        for x in r:
            print(f'{x:2}', end = ' ')
        print()

ns('print a "2d array" of numbers 1 to 10')
a = []
for i in range(1, 10):
    the_end = ' '
    if i % 3 == 0:
        the_end = '\n'
    print(i, end=the_end)


w = 2
h = 3

ns('create a 2d array such that a[i,j] increases by one each time')
a = [[w*i+j for j in range(w)] for i in range(h)]
print2d(a)

ns('create a 2d array such that a[i,j] increases by one each time')
print('start from 1 this time')
b = [[w*i+(j+1) for j in range(w)] for i in range(h)]
print2d(b)

ns('what is the zip of a and b?')
for x in zip(a,b): 
    print (x)
    
ns('transpose a 2d array with zip')
ta = (x for x in zip(*a))
print2d(ta)

ns('dot product ok!')
a = range(3)
b = range(3,6)
assert sum(x*y for x,y in zip(a,b)) == 14

ns('random matrices')
def rand_matrix(h, w):
    return [[random.randint(0,9) for c in range(w)] for r in range(h)]
# a = rand_matrix(3,4)
# b = rand_matrix(4,2)
# print(a)
# print(b)
a = [[4, 1, 4, 4], [0, 8, 8, 6], [4, 3, 7, 2]]
b = [[7, 7], [3, 2], [9, 0], [4, 1]]
ns('matrix multiply')
def mat_mult(a, b):
    rcnt = len(a)
    ccnt = len(b[0])
    mcnt = len(a[0])
    c = [[0 for jj in range(ccnt)] for i in range(rcnt)]
    for i in range(rcnt):
        for j in range(ccnt):
            for k in range(mcnt):
                c[i][j] += a[i][k] * b[k][j]
    return c
    
c = mat_mult(a,b)
print(c)

ns('matrix multiply...pythonized!')
def mat_mult2(a, b):
    rcnt = len(a)
    ccnt = len(b[0])
    c = [[0 for jj in range(ccnt)] for i in range(rcnt)]
    for i in range(rcnt):
        for j in range(ccnt):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(len(a[0])))
    return c
    
c2 = mat_mult2(a,b)
assert c == c2


ns('matrix multiply...pythonized2!')
def vector_sum(l):
    return [sum(x) for x in zip(*l)]
def scalar_mult(x, v):
    return [x*y for y in v]
def mat_mult3(a, b):
    return [vector_sum(scalar_mult(x, v) for x,v in zip(w, b)) for w in a]
    
c3 = mat_mult3(a,b)
print(c3)
assert c == c2 == c3