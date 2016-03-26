# TODO: proper header

import sdl2
import sdl2.ext
from .state import *

def esperacualquiertecla():
    if state.SCREEN == False:
        return False

    running = True
    while running:
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYUP:
                running = False
                break
    return True    


if __name__ == "__main__":
    print ("This module is not meant to be executed")