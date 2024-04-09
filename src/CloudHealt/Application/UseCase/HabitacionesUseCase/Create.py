from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort as Port
from src.CloudHealt.Domain.Entity.Habitaciones import Habitaciones


class Create:
    def __init__(self, repository: Port):
        self.repository = repository

    def run(self, data):
        try:
            inicio = data["inicio"]
            cantidad = data["cantidad"]
            area = data["area"]
            final = inicio + cantidad
            habitaciones= []
            for i in range(inicio, final):
                habitacion = Habitaciones(i, area)
                habitaciones.append(habitacion)
            return self.repository.create_habitaciones(habitaciones)
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
