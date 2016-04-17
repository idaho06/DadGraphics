# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import dadgraphics

class  Test01TestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Test01()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_iniciapantalla(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        #self.assertEqual(dadgraphics.SCREEN,False,'Todavia no existe la pantalla creada')
        #self.assertEqual(repr(dadgraphics.iniciapantalla()),'iniciapantalla()','iniciapantalla existe')
        #self.fail("TODO: Write test")
        self.assertEqual(dadgraphics.imprimescreen(),False,'')
        dadgraphics.iniciapantalla()
        self.assertEqual(dadgraphics.imprimescreen(),True,'')
        dadgraphics.quitapantalla()
        self.assertEqual(dadgraphics.imprimescreen(),False,'')
        dadgraphics.iniciapantalla()
        self.assertEqual(dadgraphics.imprimescreen(),True,'')
        dadgraphics.quitapantalla()
        self.assertEqual(dadgraphics.imprimescreen(),False,'')
        dadgraphics.iniciapantalla(ancho=320,alto=200,pantallacompleta=False,titulo="Pantalla de 320x200")
        self.assertEqual(dadgraphics.state.SIZE,(320,200),'')
        dadgraphics.esperacualquiertecla()
        dadgraphics.quitapantalla()
        self.assertEqual(dadgraphics.state.SCREEN, False, '')
        self.assertEqual(dadgraphics.state.RENDERER, None, '')
        self.assertEqual(dadgraphics.state.WINDOW, None, '')
        self.assertEqual(dadgraphics.state.SPRITEFACTORY, None, '')
        self.assertEqual(dadgraphics.state.SPRITERENDERER, None, '')
        self.assertEqual(dadgraphics.state.WORLD, None, '')
        self.assertEqual(dadgraphics.state.RESOURCES, None, '')
        self.assertEqual(dadgraphics.state.SIZE, None, '')

    
    def test_esperatecla(self):
        self.assertEqual(dadgraphics.esperacualquiertecla(),False,'')
        dadgraphics.iniciapantalla()
        print("Pulsa cualquier tecla")
        self.assertEqual(dadgraphics.esperacualquiertecla(),True,'')
        dadgraphics.quitapantalla()
    
    def test_borrapantalla(self):
        self.assertEqual(dadgraphics.borrapantalla(),False,'')
        dadgraphics.iniciapantalla()
        self.assertEqual(dadgraphics.borrapantalla(),True,'')
        dadgraphics.esperacualquiertecla()
        self.assertEqual(dadgraphics.borrapantalla(color=dadgraphics.ROJO),True,'')
        dadgraphics.esperacualquiertecla()
        self.assertEqual(dadgraphics.borrapantalla(color=dadgraphics.VERDE),True,'')
        dadgraphics.esperacualquiertecla()
        self.assertEqual(dadgraphics.borrapantalla(color=dadgraphics.AZUL),True,'')
        dadgraphics.esperacualquiertecla()
        dadgraphics.quitapantalla()
        

if __name__ == '__main__':
    unittest.main()

