class A:
    globb = 'global'
    @classmethod
    def set(cls):
        cls.globb = 42
    @classmethod
    def echo(cls):
        print(cls.globb)
       
A.echo()       
a = A()
a.set()
A.echo()