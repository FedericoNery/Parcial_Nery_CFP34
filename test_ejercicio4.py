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

class ejercicio4TestCase(unittest.TestCase):
    def test_is_vacio_seDeterminaCampeon(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([]),"")

    def test_is__a1_b0__seDeterminaCampeon(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",0)]),'a')

    def test_is__a1_b1__a1_c1__c1_b1__seDeterminaCampeon(self):
        self.assertIn(ejercicio4.calcularGanadorDeLiga([("a",1,"b",1),("a",1,"c",1),("c",1,"b",1)]),['c','b','a'])

    def test_is__a1_b0__a1_c2__c3_b0__seDeterminaCampeon(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",0),("a",1,"c",2),("c",3,"b",0)]),'c')

    def test_is__a1_bmenos2__a1_c1__c1_b1__d1_a9__seDeterminaCampeon(self):
        self.assertEquals(ejercicio4.calcularGanadorDeLiga([("a",1,"b",-2),("a",1,"c",1),("c",1,"b",1),("d",1,"a",9)]),'a')

unittest

