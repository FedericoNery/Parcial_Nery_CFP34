import unittest
import ejercicio1
"""
print(ejercicio1("",[1,2,3])) # []
print(ejercicio1(-1,[1,2,3])) # []
print(ejercicio1(0,[1,2,3])) # []
print(ejercicio1(0,[])) # []
print(ejercicio1(1,[1,2])) # [1]
print(ejercicio1(2,[1,-2])) # [1,-2]
print(ejercicio1(8,[1,7,2,-4,6,9])) # [1,2,-4]
print(ejercicio1(331,[1,2,3,7,147,331,518])) # [1,331]
"""


class StringsTestCase(unittest.TestCase):
    def test_is_vacio_un_divisor(self):
        self.assertIsNone(ejercicio1.generarListaDivisores("",[1,2,3],"Es vacio"))

    def test_is_numNegativo_un_divisor(self):
        self.assertIsNone(ejercicio1.generarListaDivisores(-1,[1,2,3]),"Es vacio")

    def test_is_cero_un_divisor(self):
        self.assertIsNone(ejercicio1.generarListaDivisores(0,[1,2,3]),"Es vacio")

    def test_is_cero_un_divisor_de_lista_sin_multiplos(self):
        self.assertIsNone(ejercicio1.generarListaDivisores(0,[]),"Es vacio")

    def test_is_uno_un_divisor(self):
        self.assertIn(ejercicio1.generarListaDivisores(1,[1,2]),1,"Contiene Uno")

    def test_is_dos_un_divisor(self):
        self.assertEquals(ejercicio1.generarListaDivisores(2,[1,-2]))

    def test_is_ocho_un_divisor(self):
        self.assertEquals(ejercicio1.generarListaDivisores(8,[1,7,2,-4,6,9]))

    def test_is_trescientostreintayuno_un_divisor(self):
        self.assertEquals(ejercicio1.generarListaDivisores(331,[1,2,3,7,147,331,518]))

unittest