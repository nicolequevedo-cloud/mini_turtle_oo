from mini_tracker_oo import Tracker

tracker = Tracker()

tracker.iniciar_tarea("Estudiar Python")
tracker.detener_tarea(2.5)

tracker.iniciar_tarea("Hacer tarea")
tracker.detener_tarea(1.5)

print(f"Tiempo total trabajado: {tracker.consultar_total()} horas")
