# TODO: proper header

from .colores import *
import sdl2
import sdl2.ext
from .state import *

def borrapantalla(color=BLANCO):
    if state.SCREEN == False:
        return False
    lastcolor = state.RENDERER.color
    state.RENDERER.color = color
    state.RENDERER.clear(color=color)
    state.RENDERER.color = lastcolor
    state.WORLD.process()
    return True

if __name__ == "__main__":
    print ("This module is not meant to be executed")
