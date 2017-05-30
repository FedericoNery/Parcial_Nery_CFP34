import unittest
import ejercicio2

"""
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg'])) # False
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','txt'])) # True
print(ejercicio2('/home/user/listado.txt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.tXt',['mp3','wav','mpeg','TXT'])) # True
print(ejercicio2('/home/user/listado.txt',['txt'])) # True
print(ejercicio2('/home/user/listado',['mp3','wav','mpeg','txt'])) # False
print(ejercicio2('/home/user/listado',[])) # False
print(ejercicio2('',[])) # False
"""

class VerificoSiElFormatoDeLaExtensionEsValidoTestCase(unittest.TestCase):

    def test_devuelveFalsoSiLaExtension_txt_NoSeEncuentraEnLaListaDeExtensiones(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg']),"Es Falso")

    def test_devuelveVerdaderoSiLaExtension_txt_SeEncuentraEnLaListaDeExtensiones(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg','txt']),"Es Verdadero")

    def test_devuelveVerdaderoSiLaExtension_TXT_SeEncuentraEnLaListaDeExtensiones(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg','TXT']),"Es Verdadero")

    def test_devuelveVerdaderoSiLaExtension_tXt_SeEncuentraEnLaListaDeExtensiones(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.tXt',['mp3','wav','mpeg','TXT']),"Es Verdadero")

    def test_devuelveVerdaderoSiLaExtension_txt_SeEncuentraEnLaListaDeExtensiones(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['txt']),"Es Verdadero")

    def test_devuelveFalsoSiNoSeEncuentraLaExtensionDelArchivo(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado',['mp3','wav','mpeg','txt']),"Es Falso")

    def test_devuelveFalsoSiNoSeEncuentraLaExtensionDelArchivoYSiLaListaDeExtensionesEsVacia(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado',[]),"Es Falso")

    def test_devuelveFalsoSiNoSePasaLaExtensionDelArchivoYSiLaListaDeExtensionesEsVacia(self):
        self.assertFalse(ejercicio2.validarExtension('',[]),"Es Falso")

unittest
