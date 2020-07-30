from filters.blur import BlurFilter
from filters.inverted import InvertedFilter
from filters.sepia import SepiaFilter
from filters.black_and_white import BlackAndWhite
import sys


class NoSuchFilter(Exception):
    """"Exception raised for invalid command line arguments"""

    def __init__(self, message='Invalid filter!'):
        self.message = message
        super().__init__(self.message)

if sys.argv[1] == 'black_and_white':
    bw = BlackAndWhite()
    bw.execute_filter()
elif sys.argv[1] == 'blur':
    blur = BlurFilter()
    blur.execute_filter()
elif sys.argv[1] == 'sepia':
    sepia = SepiaFilter()
    sepia.execute_filter()
elif sys.argv[1] == 'inverted':
    inverted = InvertedFilter()
    inverted.execute_filter()

else:
    raise NoSuchFilter
