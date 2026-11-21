import csv
import os
import matplotlib.pyplot as plt

class MesaDeAyuda:
    def __init__(self, tickets, mu=10.0):
        # Ordenamos los tickets segun el minuto de llegada
        self.tickets = sorted(tickets, key=lambda t: t["llegada"])
        self.mu = float(mu)
        self.historial = []

    def tasa_llegadas(self):
        # 8 tickets observados en una hora
        return float(len(self.tickets))

    def metricas_mm1(self, lam=None):
        if lam is None:
            lam = self.tasa_llegadas()
        rho = lam / self.mu
        lq = (rho ** 2) / (1 - rho)
        wq = rho / (self.mu - lam)
        return {
            "lambda": lam,
            "mu": self.mu,
            "rho": rho,
            "Lq": lq,
            "Wq": wq
        }

    def simular(self):
        self.historial = []
        fin_anterior = 0
        for t in self.tickets:
            codigo = t["codigo"]
            llegada = t["llegada"]
            atencion = t["atencion"]
            # Si el servidor esta desocupado al llegar el ticket, inicia de inmediato
            inicio = max(llegada, fin_anterior)
            fin = inicio + atencion
            espera = inicio - llegada
            fin_anterior = fin
            self.historial.append({
                "Ticket": codigo,
                "Llegada": llegada,
                "Atencion": atencion,
                "Inicio": inicio,
                "Fin": fin,
                "Espera": espera
            })
        esperas = [fila["Espera"] for fila in self.historial]
        promedio = sum(esperas) / len(esperas)
        return {
            "detalle": self.historial,
            "esperas": esperas,
            "promedio_espera_minutos": promedio
        }

    def mostrar_tabla(self):
        print(f"\n{'Ticket':<8}{'Llegada':<10}{'Atencion':<10}{'Inicio':<8}{'Fin':<8}{'Espera':<8}")
        print("-" * 52)
        for f in self.historial:
            print(f"{f['Ticket']:<8}{f['Llegada']:<10}{f['Atencion']:<10}{f['Inicio']:<8}{f['Fin']:<8}{f['Espera']:<8}")

    def guardar_csv(self, ruta="resultado_simulacion.csv"):
        if not self.historial:
            return
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.historial[0].keys())
            writer.writeheader()
            writer.writerows(self.historial)

    def graficar(self, ruta="graficas/resultado.png"):
        if not self.historial:
            self.simular()
        tickets = [f["Ticket"] for f in self.historial]
        esperas = [f["Espera"] for f in self.historial]
        promedio = sum(esperas) / len(esperas)
        plt.figure(figsize=(8, 4))
        plt.bar(tickets, esperas, color="skyblue", edgecolor="navy")
        plt.axhline(promedio, color="red", linestyle="--", label=f"Promedio: {promedio:.2f} min")
        plt.title("Tiempos de Espera por Ticket - MatriculApp")
        plt.xlabel("Tickets")
        plt.ylabel("Minutos de espera")
        plt.legend()
        plt.grid(axis="y", linestyle=":")
        plt.tight_layout()
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        plt.savefig(ruta)
        plt.close()
