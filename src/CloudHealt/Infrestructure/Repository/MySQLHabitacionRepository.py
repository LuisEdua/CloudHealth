from src.CloudHealt.Infrestructure.Models.MySQLHabitacionesModel import MySQLHabitacionesModel as Model
from src.CloudHealt.Domain.Ports.HabitacionesPort import HabitacionesPort
from src.CloudHealt.Domain.Entity.Habitaciones import Habitaciones
from src.Database.MySQL import Base, engine, session_local


class MySQLHabitacionRepository(HabitacionesPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_habitaciones(self, area_uuid):
        try:
            habitaciones = self.db.query(Model).filter(Model.area_uuid == area_uuid).all()
            if habitaciones:
                return {"message": "Habitaciones found", "habitaciones": [h.to_json() for h in habitaciones],
                        "status": "Success"}, 200
            else:
                return {"message": "Habitaciones not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "Error"}, 500

    def get_all_habitaciones(self):
        try:
            habitaciones = self.db.query(Model).all()
            if habitaciones:
                return {"message": "Habitaciones found", "habitaciones": [h.to_json() for h in habitaciones],
                        "status": "Success"}, 200
            else:
                return {"message": "Habitaciones not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "Error"}, 500

    def create_habitaciones(self, habitaciones: list[Habitaciones]):
        try:
            news = [Model(uuid=h.uuid, number=h.number, area_uuid=h.area) for h in habitaciones]
            self.db.add_all(news)
            self.db.commit()
            return {"message": "Habitaciones created successfully", "habitaciones": [h.to_json() for h in news],
                    "status": "Success"}, 201
        except Exception as e:
            return {"message": str(e), "status": "Error"}, 500
