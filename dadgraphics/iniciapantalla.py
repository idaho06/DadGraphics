# TODO: proper header

import sdl2
import sdl2.ext
from .state import *


def iniciapantalla(ancho=640, alto=480, pantallacompleta=False, titulo="Dadgraphics version 0.1"):
    if state.SCREEN == False:
        if pantallacompleta:
            sdlflags=sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
        else:
            sdlflags=None
            
        state.RESOURCES = sdl2.ext.Resources(__file__, "./res")
        sdl2.ext.init()
        #window = sdl2.ext.Window("Up, up and above remake", size=(800, 600), flags=sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP)
        state.WINDOW = sdl2.ext.Window(titulo, size=(ancho, alto), flags=sdlflags)
        state.WINDOW.show()
        #logging.info('SDL window started')

        #logging.info('Setting world')
        state.WORLD = sdl2.ext.World()

        #logging.info('Creating renderer')
        state.RENDERER = sdl2.ext.Renderer(state.WINDOW,flags=sdl2.render.SDL_RENDERER_ACCELERATED|sdl2.render.SDL_RENDERER_PRESENTVSYNC)
        #logging.info('Creating sprite factory')
        state.SPRITEFACTORY = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE, renderer=state.RENDERER)
    
        state.SCREEN = True
        return True
    else:
        printf("La pantalla ya esta creada")
        return false
    
if __name__ == "__main__":
    print ("This module is not meant to be executed")
