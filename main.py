from filters.blur import execute_blur
from filters.inverted import execute_inverted
from filters.sepia import execute_sepia
from filters.black_and_white import execute_black_and_white
import sys


class NoSuchFilter(Exception):
    """"Exception raised for invalid command line arguments"""

    def __init__(self, message='Invalid filter!'):
        self.message = message
        super().__init__(self.message)


if sys.argv[1] == 'black_and_white':
    execute_black_and_white()
elif sys.argv[1] == 'blur':
    execute_blur()
elif sys.argv[1] == 'sepia':
    execute_sepia()
elif sys.argv[1] == 'inverted':
    execute_inverted()
else:
    raise NoSuchFilter
