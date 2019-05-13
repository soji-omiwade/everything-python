from .. import zoo
print('start {1} from pkg {0}'.format(__package__, __name__))
print(zoo.shoe(42))
print(f'end {__name__}')
