"""
this class implements the reversing of a list using: 
(i) an iterator class, and
(ii) a counter within the iterator class
"""
class reverse_list_iterator:
    def __init__(self, l):
        self.l = l
        self.index  = 0
    def __next__(self):
        if self.index >= len(self.l):
            raise StopIteration
        val = self.l[len(self.l)-(self.index+1)]
        self.index += 1
        return val

class reverse_list:
    def __init__(self, l):
        self.l = l
    def __iter__(self):
        return reverse_list_iterator(self.l)
        
l = [3,89,5,1,1,42]
out = []
for i in reverse_list(l):
    out.append(i)
print(', '.join(str(i) for i in out))
print('hmmm...', 'i think we"ve changed the original list though')
print(l)
#wow. the original list isn't changed