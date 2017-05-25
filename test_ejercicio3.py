import unittest
import ejercicio3
"""
print(ejercicio3(-1)) # []
print(ejercicio3(0)) # []
print(ejercicio3(1)) # []
print(ejercicio3(2)) # [[x,x],[0,x]]
print(ejercicio3(3)) # [[x,x,x],[0,x,x],[0,0,x]]
print(ejercicio3(4)) # [[x,x,x,x],[0,x,x,x],[0,0,x,x],[0,0,0,x]]
print(ejercicio3("4")) #[]
print(ejercicio3("PEPE")) #[]
print(ejercicio3(2.5)) #[]
"""

class ejercicio3TestCase(unittest.TestCase):

    def test_is_menosUno_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(-1),[])

    def test_is_cero_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(0),[])

    def test_is_uno_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(1),[])

    def test_is_dos_generaMatriz(self):
        self.assertEquals((ejercicio3.generarMatrizTriangular(2))[1][0],0)

    def test_is_tres_generaMatriz(self):

        for h in range(0,3):
            for i in range(0,3):
                if ((h > 0) and (h - i > 0)):
                    self.assertEquals(ejercicio3.generarMatrizTriangular(3)[h][i], 0)
                #else:



    def test_is_cuatro_generaMatriz(self):
        for h in range(0,4):
            for i in range(0,4):
                if ((h > 0) and (h - i > 0)):
                    self.assertEquals(ejercicio3.generarMatrizTriangular(4)[h][i], 0)

    def test_is_cuatroString_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular("4"),[])

    def test_is_pepeString_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular("PEPE"),[])

    def test_is_dosYUnMedio_generaMatriz(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(2.5),[])

unittest