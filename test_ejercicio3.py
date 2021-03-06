import unittest
import ejercicio3

class VerificoGeneracionCorrectaDeMatricesTestCase(unittest.TestCase):

    def test_devuelveListaVaciaSiElArgumentoEsUnNumeroNegativo(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(-1),[])

    def test_devuelveListaVaciaSiElArgumentoEsCero(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(0),[])

    def test_devuelveListaVaciaSiElArgumentoEsUno(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(1),[])

    def test_devuelveLaMatrizDeDosPorDosSiElArgumentoEsDos(self):
        self.assertEquals((ejercicio3.generarMatrizTriangular(2))[1][0],0)

    def test_devuelveLaMatrizDeTresPorTresSiElArgumentoEsTres(self):

        for h in range(0,3):
            for i in range(0,3):
                if ((h > 0) and (h - i > 0)):
                    self.assertEquals(ejercicio3.generarMatrizTriangular(3)[h][i], 0)
                #else:

    def test_devuelveLaMatrizDeCuatroPorCuatroSiElArgumentoEsCuatro(self):
        for h in range(0,4):
            for i in range(0,4):
                if ((h > 0) and (h - i > 0)):
                    self.assertEquals(ejercicio3.generarMatrizTriangular(4)[h][i], 0)

    def test_devuelveUnaListaVaciaSiElArgumentoEsUnCaracter(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular("4"),[])

    def test_devuelveUnaListaVaciaSiElArgumentoEsUnString(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular("PEPE"),[])

    def test_devuelveUnaListaVaciaSiElNumeroEsUnFlotante(self):
        self.assertEquals(ejercicio3.generarMatrizTriangular(2.5),[])