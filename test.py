import unittest
from examen import *

class Pruebas(unittest.TestCase):

    def test_libros(self):
        libros = [Libro(Autor(1, "pepe", "pepon"), "Pepe aventuras", 1920), Libro(Autor(1, "pepe", "pepon"), "Aventuras de pepo", 1922), Libro(Autor(2, "pepa", "pepon"), "Pepa's Adventure", 1922)]
        self.assertEqual(mas_antiguos(libros, 1901), [])
        self.assertEqual(mas_antiguos(libros, 1920), ["Pepe aventuras"])
        self.assertEqual(mas_antiguos(libros, 1922), ["Aventuras de pepo","Pepa's Adventure"])
        
class Suite(unittest.TestSuite):
    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_libros'))

if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)