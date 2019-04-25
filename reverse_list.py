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

        
if __name__ == '__main__':
    rli = iter(reverse_list([3,89,5,1,1,42]))
    for i in rli:
        print(i, ',')