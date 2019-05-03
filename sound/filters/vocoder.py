print('running module', __name__)
import sys
from . import equalizer
from ..effects import echo
print('mis vocoder')
my_vocoder = 'mi vocoder'

echo_vocoder = echo.echofilter('vocoder-input', 42, 43, foo=my_vocoder)

try: 
    echofilter(1,2)
except Exception as e: 
    print('exception: ', e)
    
from ..effects.echo import echofilter
echofilter(1,2)