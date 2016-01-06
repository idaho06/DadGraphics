# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from iniciapantalla import *

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
        self.assertEqual(repr(iniciapantalla()),'iniciapantalla()','iniciapantalla existe')
        #self.fail("TODO: Write test")

if __name__ == '__main__':
    unittest.main()

