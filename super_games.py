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
class B(A):
    def __init__(self):
        self.me = 'b'
        print('B object', self, 'created')
    def pooh(self):
        return (self,'B:pooh')
    def echo(self):
        print(super(B, self).pooh()) #this hits A's pooh, not B's!!!
        
        #notes
        print(A.pooh(self) == super(B, self).pooh()) #True!
        #which means 
        # print(super(A, self).pooh())
        
class C(B):
    def __init__(self):
        self.me = 'c'
        print('C object', self, 'created')
    def pooh(self):
        return (self,'C:pooh')
    def echo(self):
        print(B.pooh(self))
        print(super(C, self).pooh() == B.pooh(self)) 
        print(A.pooh(self))
        print(super(B, self).pooh() == A.pooh(self)) 

b = B()
b.echo()
print()
c = C()
c.echo()