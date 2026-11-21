import sys
import os
# Permite ejecutar desde la raiz o desde la carpeta src sin fallar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from src.modelo import MesaDeAyuda
except ModuleNotFoundError:
    from modelo import MesaDeAyuda

from pymongo import MongoClient

def cargar_datos_mongo():
    try:
        cliente = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
        db = cliente["huilasoft"]
        agente = db.agentes.find_one({"turno": True})
        mu = float(agente["tickets_hora"]) if agente else 10.0
        tickets = list(db.tickets.find())
        if tickets:
            return tickets, mu
        print("No se encontraron tickets en la BD. Usando lista de respaldo.")
    except Exception as error:
        print(f"Aviso de conexion: {error}. Se usaran los datos locales.")
    # Datos del caso si MongoDB no esta iniciado
    mu = 10.0
    tickets = [
        {"codigo": "T1", "llegada": 0, "atencion": 5},
        {"codigo": "T2", "llegada": 3, "atencion": 7},
        {"codigo": "T3", "llegada": 6, "atencion": 4},
        {"codigo": "T4", "llegada": 14, "atencion": 8},
        {"codigo": "T5", "llegada": 25, "atencion": 6},
        {"codigo": "T6", "llegada": 28, "atencion": 5},
        {"codigo": "T7", "llegada": 40, "atencion": 9},
        {"codigo": "T8", "llegada": 52, "atencion": 4}
    ]
    return tickets, mu

if __name__ == "__main__":
    tickets, mu = cargar_datos_mongo()
    print("=" * 45)
    print("MESA DE AYUDA HUILASOFT - OPCION A")
    print("=" * 45)
    print(f"Servidor: Laura Cerquera (mu = {mu} tickets/hora)")
    print(f"Tickets recibidos: {len(tickets)}")
    mesa = MesaDeAyuda(tickets, mu)
    # 1. Calculos de la formula M/M/1
    teoria = mesa.metricas_mm1()
    print("\nResultados del modelo teorico M/M/1:")
    print("-" * 45)
    print(f"Llegadas (lambda): {teoria['lambda']:.1f} tickets/h")
    print(f"Factor de uso (rho): {teoria['rho']:.2f}")
    print(f"Longitud cola (Lq): {teoria['Lq']:.2f} tickets")
    print(f"Tiempo de espera (Wq): {teoria['Wq']:.2f} h ({teoria['Wq'] * 60:.1f} min)")
    # Escenario de aumento de demanda
    pico = mesa.metricas_mm1(lam=9.5)
    print(f"\nEscenario con demanda pico (lambda = 9.5):")
    print("-" * 45)
    print(f"Nuevo uso (rho): {pico['rho']:.2f}")
    print(f"Nueva espera (Wq): {pico['Wq']:.2f} h ({pico['Wq'] * 60:.1f} min)")
    # 2. Simulacion paso a paso (se ejecuta una sola vez)
    resumen = mesa.simular()
    mesa.mostrar_tabla()
    print("-" * 52)
    print(f"Tiempo promedio de espera en simulacion: {resumen['promedio_espera_minutos']:.3f} minutos")
    # 3. Exportar resultados y generar grafica
    mesa.guardar_csv("resultado_simulacion.csv")
    mesa.graficar("graficas/resultado.png")
    print("\nResultados exportados a CSV y grafica guardada en 'graficas/resultado.png'.")
