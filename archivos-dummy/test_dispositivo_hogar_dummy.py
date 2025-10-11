import pytest
# Importa del dummy específico (evita conflicto con real)
from dispositivo_hogar_dummy import DispositivoHogar


def test_get_id_dispositivo():
    dispositivo = DispositivoHogar("dev001", 1, "Sala", "10:00", "Luz", "iluminacion", "Philips", 25.0, False)
    assert dispositivo.get_id_dispositivo() == "dev001"
