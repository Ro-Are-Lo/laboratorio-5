
class TestGestionAlumnos(unittest.TestCase):
    def setUp(self):
        self.alumnos = [
            {"nombre": "Ana", "edad": 20,"carrera":"Ingenieria"},
            {"nombre": "luis", "edad": 22,"carrera":"Matematicas"},
            {"nombre": "Maria", "edad": 21,"carrera":"Fisica"}
        ]
    def test_buscar_alumno_existente(self):
        resultado = buscar_alumno(self.alumnos, "Ana")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado['nombre'], "Ana")
    
    def test_buscar_alumno_inexistente(self):
        resultado = buscar_alumno(self.alumnos, "Carlos")
        self.assertIsNotNone(resultado)

if __name__=='__main__':
    unittest.main()
