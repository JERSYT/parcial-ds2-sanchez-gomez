import sys
import os
# Permite ejecutar desde la raiz o desde la carpeta tests sin fallar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.modelo import MesaDeAyuda

TICKETS_PRUEBA = [
    {"codigo": "T1", "llegada": 0, "atencion": 5},
    {"codigo": "T2", "llegada": 3, "atencion": 7},
    {"codigo": "T3", "llegada": 6, "atencion": 4},
    {"codigo": "T4", "llegada": 14, "atencion": 8},
    {"codigo": "T5", "llegada": 25, "atencion": 6},
    {"codigo": "T6", "llegada": 28, "atencion": 5},
    {"codigo": "T7", "llegada": 40, "atencion": 9},
    {"codigo": "T8", "llegada": 52, "atencion": 4}
]

def test_metricas_mm1():
    # Prueba con lambda=8 y mu=10 dada en el parcial
    mesa = MesaDeAyuda(TICKETS_PRUEBA, mu=10.0)
    metricas = mesa.metricas_mm1(lam=8.0)
    assert round(metricas["rho"], 2) == 0.80
    assert round(metricas["Lq"], 2) == 3.20
    assert round(metricas["Wq"], 2) == 0.40

def test_simulacion():
    # Verifica esperas individuales y promedio de 1.625 min
    mesa = MesaDeAyuda(TICKETS_PRUEBA, mu=10.0)
    resultado = mesa.simular()
    esperas = resultado["esperas"]
    assert esperas == [0, 2, 6, 2, 0, 3, 0, 0]
    assert abs(resultado["promedio_espera_minutos"] - 1.625) < 0.001

if __name__ == "__main__":
    test_metricas_mm1()
    test_simulacion()
    print("Todas las pruebas pasaron correctamente.")
