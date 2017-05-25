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

class ejercicio2TestCase(unittest.TestCase):
    def test_is__home_user_listado_txt__mp3_wav_mpeg__un_formato_valido(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg']),"Es Falso")

    def test_is__home_user_listado_txt__mp3_wav_mpeg_txt__un_formato_valido(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg','txt']),"Es Verdadero")

    def test_is__home_user_listado_txt__mp3_wav_mpeg_TXT__un_formato_valido(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['mp3','wav','mpeg','TXT']),"Es Verdadero")

    def test_is__home_user_listado_tXt__mp3_wav_mpeg_TXT__un_formato_valido(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.tXt',['mp3','wav','mpeg','TXT']),"Es Verdadero")

    def test_is__home_user_listado_txt__txt__un_formato_valido(self):
        self.assertTrue(ejercicio2.validarExtension('/home/user/listado.txt',['txt']),"Es Verdadero")

    def test_is__home_user_listado__mp3_wav_mpeg_txt__un_formato_valido(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado',['mp3','wav','mpeg','txt']),"Es Falso")

    def test_is__home_user_listado__vacio__un_formato_valido(self):
        self.assertFalse(ejercicio2.validarExtension('/home/user/listado',[]),"Es Falso")

    def test_is__vacio__vacio__un_formato_valido(self):
        self.assertFalse(ejercicio2.validarExtension('',[]),"Es Falso")

unittest
