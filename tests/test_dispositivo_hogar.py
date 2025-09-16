import unittest
from modelos.dispositivo_hogar import DispositivoHogar

class TestDispositivoHogar(unittest.TestCase):
    def test_encender_apagar(self):
        d = DispositivoHogar("a123", "apagado", True)
        d.encender()
        self.assertEqual(d.estado_dispositivo, "encendido")
        d.apagar()
        self.assertEqual(d.estado_dispositivo, "apagado")

    def test_es_esencial(self):
        d = DispositivoHogar("a123", "Luz", True)
        self.assertTrue(d.es_esencial())