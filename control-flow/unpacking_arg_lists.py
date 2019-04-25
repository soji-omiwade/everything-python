def unpack_list_and_tuple(a, b):
    args = [a, b]
    tuple_args = (2*a,3*b)
    a = (list(range(*args)))
    b = (list(range(*tuple_args)))
    print(a, b)
    
def unpack_from_params(*args):
    for x in args:
        print(x, end = ', ')
    print()
    
if __name__ == '__main__':
    # unpack_list_and_tuple(2, 5)
    unpack_from_params([1,2], 42, '42')
    a = ([1,2], 42, '42')
    unpack_from_params(a)
    unpack_from_params(*a)