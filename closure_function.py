def print_msg(msg):
    def printer():
        print(msg)
    return printer
a = print_msg('hello')
b = print_msg('bye')
b()
b()
a()
