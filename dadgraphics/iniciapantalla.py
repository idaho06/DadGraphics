# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sdl2
import sdl2.ext

class iniciapantalla:
    def __init__(self, ancho=640, alto=480, pantallacompleta=True):
        #print ('ancho:%d, alto:%d', ancho, alto)
        self._iniciapantalla(ancho, alto, pantallacompleta)
    
    def __repr__(self):
        return 'iniciapantalla()'

    def _iniciapantalla(self, ancho, alto, pantallacompleta):
        pass

if __name__ == "__main__":
    print ("This module is not meant to be executed")
