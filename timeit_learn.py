import timeit
from pretty_print import next_sample as ns

ns('time list.sort')
setup = """
import random
random.seed()
s = [random.random() for i in range(1000)]
"""
for i in timeit.Timer('a = s[:]; list.sort(a)', setup=setup).repeat(7, 1000):
    print(i)
    
ns('time map and zip and izip')
setup = '''
import random
from operator import add
random.seed(42)
list1 = [random.randint(0, 100_000) for _ in range(100_000)]
list2 = [random.randint(0, 100_000) for _ in range(100_000)]
'''
by_map = 'map(add, list1, list2)'
by_zip = '(x+y for x,y in zip(list1, list2))'
repeat = 7
num = 1000
print(min(timeit.Timer(by_map, setup = setup).repeat(repeat, num)))
print(min(timeit.Timer(by_zip, setup = setup).repeat(repeat, num)))
