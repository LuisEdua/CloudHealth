from src.CloudHealt.Domain.Ports.PisosPort import PisosPort
from src.CloudHealt.Domain.Entity.Pisos import Pisos
from src.CloudHealt.Infrestructure.Models.MySQLPisosModel import MySQLPisosModel as Model
from src.Database.MySQL import Base, engine, session_local


class MySQLPisoRepository(PisosPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_pisos(self):
        try:
            pisos = self.db.query(Model).all()
            if pisos:
                return {"message": "Pisos found", "pisos":[p.to_json() for p in pisos], "status": "Success"}, 200
            else:
                return {"message": "Not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def create_pisos(self, piso: Pisos):
        try:
            new = Model(uuid=piso.uuid, level=piso.level)
            self.db.add(new)
            self.db.commit()
            return {"message": "Piso added successfully", "pisos":new.to_json()}, 201
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
