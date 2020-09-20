import unittest
import index 
class TestMyModule(unittest.TestCase):
    def test_index_procs(self):
        print("RESULTADO DE LA PRUEBA: FUNCION index.procs()")
        self.assertTrue(index.procs())

if __name__ == "__main__":
    print("-----------------------------------------")
    print("PRUEBAS UNITARIAS DEL PROYECTO ZINOBE")
    print("-----------------------------------------\n\n")
    unittest.main()





