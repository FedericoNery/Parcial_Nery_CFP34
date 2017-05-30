import unittest
import ejercicio4

"""
campeonato = []
print(ejercicio4(campeonato)) # ""

campeonato = [("a",1,"b",0)]
print(ejercicio4(campeonato)) # a

campeonato = [("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]
print(ejercicio4(campeonato)) # c

campeonato = [("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]
print(ejercicio4(campeonato)) # a  b  c (cualquiera de las 3)

campeonato = [("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]
print(ejercicio4(campeonato)) # a
"""

class DeterminoGanadorDeLaLigaTestCase(unittest.TestCase):

    def test_devuelveStringVacioSiElArgumentoEsUnaListaVacia(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([]),"")

    def test_devuelveCaracter_a_SiElArgumentoEsUnSoloPartido(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",0)]),'a')

    def test_devuelve_a_b_c_SiElArgumentoSonTresPartidos(self):
        self.assertIn(ejercicio4.calcularGanadorDeLiga([("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]),['c','b','a'])

    def test_devuelve_c_SiElArgumentoSonTresPartidos(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]),'c')

    def test_devuelve_a_SiElArgumentoSonCuatroPartidos(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]),'a')

unittest

