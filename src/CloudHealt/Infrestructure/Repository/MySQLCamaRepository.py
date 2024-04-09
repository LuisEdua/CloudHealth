from src.CloudHealt.Domain.Entity.Camas import Camas
from src.CloudHealt.Domain.Ports.CamasPort import CamasPort
from src.CloudHealt.Infrestructure.Models.MySQLHabitacionesModel import MySQLHabitacionesModel
from src.Database.MySQL import Base, engine, session_local
from sqlalchemy.orm import joinedload
from src.CloudHealt.Infrestructure.Models.MySQLCamasModel import MySQLCamasModel as Model
from src.CloudHealt.Infrestructure.Models.MySQLPacientesModel import MySQLPacientesModels


class MySQLCamasRepository(CamasPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_free_camas(self, area_uuid):
        try:
            all_camas_in_area = (self.db.query(Model).join(MySQLHabitacionesModel)
                                 .filter(MySQLHabitacionesModel.area_uuid == area_uuid)
                                 .options(joinedload(Model.habitacion)).all())
            occupied_beds_uuids = {cama.cama_uuid for cama in self.db.query(MySQLPacientesModels.cama_uuid).all()}
            free_camas = [cama for cama in all_camas_in_area if cama.uuid not in occupied_beds_uuids]
            if free_camas:
                return {"message": "Free camas found", "free_camas": [c.to_json() for c in free_camas],
                        "status": "Success"}, 200
            else:
                return {"message": "Free camas not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def get_all_camas(self):
        try:
            camas = self.db.query(Model).all()
            if camas:
                return {"message": "Camas found", "camas": [c.to_json() for c in camas], "status": "Success"}, 200
            else:
                return {"message": "Camas not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500


    def create_camas(self, camas: list[Camas]):
        try:
            news = [Model(uuid=cama.uuid, number=cama.number, habitacion_uuid=cama.habitacion_uuid)for cama in camas]
            self.db.add_all(news)
            self.db.commit()
            return {"status": "created", "message": "Camas creates", "camas": [c.to_json() for c in news]}, 201
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
