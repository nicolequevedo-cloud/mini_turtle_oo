class Tracker:
    def __init__(self):
        self.tiempo_total_acumulado = 0.0

    def iniciar_tarea(self, tarea):
        print(f"Iniciando tarea: {tarea}")

    def detener_tarea(self, tiempo_trabajado):
        self.tiempo_total_acumulado += tiempo_trabajado
        print(f"Tarea detenida. Tiempo trabajado: {tiempo_trabajado} horas")

    def consultar_total(self):
        return self.tiempo_total_acumulado
