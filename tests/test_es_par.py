# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import es_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Tests para comprobar que la función es_par funciona correctamente
    def test_es_par():
        assert es_par(2), "2 debería ser par"
        assert not es_par(3), "3 no debería ser par"
        assert es_par(0), "0 debería ser par"
        assert not es_par(-1), "-1 no debería ser par"
        assert es_par(-2), "-2 debería ser par"
        assert not es_par(1111111111111), "1111111111111 no debería ser par"
        
        # print("Todos los tests se han pasado con éxito!")
