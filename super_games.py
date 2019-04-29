"""
super(type, obj)
    binds to all the functions from type's immediate parent, using the obj
    instancec. so it's an object (of type super). which isn't of type 
    type's imm. parent, but at the same time isn't obj. very interesting
"""
class A:
    def __init__(self):
        self.me = 'a'
        print('A object', self, 'created')
    def pooh(self):
        return (self,'A:pooh')
    @classmethod
    def glue(cls):
        return (cls, 'A:glue')
class B(A):
    def __init__(self):
        self.me = 'b'
        print('object', self, 'initialized in class ', B)
    def pooh(self):
        return str((self,'B:pooh')) + '\n----\n' + str(super().pooh())
    def echo(self):
        print(super(B, self).pooh()) 
        print(A.pooh(self) == super(B, self).pooh())
    @classmethod
    def glue(cls):
        return (cls, 'B:glue')
    @staticmethod
    def zoo():
        print('yeah')

class C(B):
    def __init__(self):
        self.mee = 'c'
        print('object', self, 'initialized in class ', C)
    def pooh(self):
        return (self,'C:pooh')
    def echo(self):
        print(B.pooh(self))
        print(super(C, self).pooh() == B.pooh(self)) 
        print(A.pooh(self))
        print(super(B, self).pooh() == A.pooh(self)) 
        print(super().pooh() == super(C, self).pooh())
b = B()
b.echo()
print()
c = C()
c.echo()