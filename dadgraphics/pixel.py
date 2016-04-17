# TODO: proper header

import sdl2
import sdl2.ext
from .state import *
from .colores import *


def pixel(x=0,y=0,color=None):
    if color is None:
        return False

    if not state.SCREEN:
        return False

    state.RENDERER.draw_point((x,y),color)
    state.WORLD.process()
    return True


if __name__ == "__main__":
    print ("This module is not meant to be executed")
