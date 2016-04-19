# TODO: proper header

import sdl2
import sdl2.ext
from .state import *
from .colores import *


def linea(x1=0, y1=0, x2=0, y2=0, color=None):
    if color is None:
        return False

    if not state.SCREEN:
        return False

    state.RENDERER.draw_line((x1, y1, x2, y2), color)
    state.RENDERER.present()
    return True


if __name__ == "__main__":
    print("This module is not meant to be executed")
