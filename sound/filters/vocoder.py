print('running module "{0}" from package "{1}"'.format(__name__, __package__))
   

"""
import filters.equalizer
. -> sound.filters
.. -> sound

note however if you do  python -m then we the relative import works. this must
be because the switch tells python to run the argument to the switch as if it
the main was running and then it did import 'arg'
""";