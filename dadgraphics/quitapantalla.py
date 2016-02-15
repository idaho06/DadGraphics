# TODO: proper header

import sdl2
import sdl2.ext
from .state import *


def quitapantalla():
    sdl2.ext.quit()
    state.WINDOW = None
    state.RENDERER = None
    state.RESOURCES = None
    state.WORLD = None
    state.SPRITEFACTORY = None
    state.SCREEN = False

if __name__ == "__main__":
    print ("This module is not meant to be executed")
