print(f'{repr(__name__)}, {repr(__package__)}: begin')
#this is the top level package
# we can initialize sound package here
print('initializing the {1} package from module {0}'\
    .format(__name__, __package__))
a = 'sound'
# from sound.effects import echo.echofilter
# moo(1)
print(f'{repr(__name__)}, {repr(__package__)}: end************')