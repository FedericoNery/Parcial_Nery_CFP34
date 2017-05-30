import unittest
import ejercicio1

class GenerarListaDivisoresTestCase(unittest.TestCase):

    def test_devuelveListaVaciaSiElDividendoEsVacio(self):
        self.assertEquals(ejercicio1.generarListaDivisores("",[1,2,3]),[])

    def test_devuelveListaVaciaSiElDividendoEsUnNumeroNegativo(self):
        self.assertEquals(ejercicio1.generarListaDivisores(-1,[1,2,3]),[])

    def test_devuelveListaVaciaSiElDividendoEsCero(self):
        self.assertEquals(ejercicio1.generarListaDivisores(0,[1,2,3]),[])

    def test_devuelveListaVaciaSiElDividendoEsCeroYLaListaDeNumeradoresEsVacia(self):
        self.assertEquals(ejercicio1.generarListaDivisores(0,[]),[])

    def test_devuelveUnoSiElDividendoEsUnoYLosNumeradoresSonUnoYDos(self):
        self.assertEquals(ejercicio1.generarListaDivisores(1,[1,2]),[1])

    def test_devuelveUnoyMenosDosSiElDividendoEsDosYLosNumeradoresSonUnoYMenosDos(self):
        self.assertEquals(ejercicio1.generarListaDivisores(2,[1,-2]),[1,-2])

    def test_devuelveUnoDosYMenosCuatroSiElDividendoEsOchoYLosNumeradoresSonUnoSieteDosMenosCuatroSeisNueve(self):
        self.assertEquals(ejercicio1.generarListaDivisores(8,[1,7,2,-4,6,9]),[1,2,-4])

    def test_devuelveUnoYTrescientosTreintaYUnoSiElDividendoEsTrescientosTreintaYUno(self):
        self.assertEquals(ejercicio1.generarListaDivisores(331,[1,2,3,7,147,331,518]),[1,331])