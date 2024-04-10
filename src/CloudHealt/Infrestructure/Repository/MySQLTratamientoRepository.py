from src.CloudHealt.Domain.Ports.TratamientosPort import TratamientosPort
from src.CloudHealt.Domain.Entity.Tratamientos import Tratamientos
from src.Database.MySQL import Base, engine, session_local
from src.CloudHealt.Infrestructure.Models.MySQLTratamientosModel import MySQLTratamientosModel as Model


class MySQLTratamientoRepository(TratamientosPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_tratamientos(self, paciente_uuid):
        try:
            tratamientos = self.db.query(Model).filter(Model.paciente_uuid == paciente_uuid).all()
            if tratamientos:
                return {"Message": "Tratamientos found successfully",
                        "Tratamientos": [tratamiento.to_json() for tratamiento in tratamientos]}, 200
            else:
                return {"Message": "Tratamientos not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500

    def create_tratamiento(self, tratamiento: Tratamientos):
        try:
            new = Model(uuid=tratamiento.uuid, title=tratamiento.title, description=tratamiento.description,
                        paciente_uuid=tratamiento.paciente_uuid)
            self.db.add(new)
            self.db.commit()
            return {"Message": "Tratamiento created successfully", "tratamiento": new.to_json(),
                    "status": "created"}, 201
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500

    def delete_tratamiento(self, uuuid):
        try:
            tratamiento = self.db.query(Model).filter_by(uuid=uuuid).first()
            self.db.delete(tratamiento)
            self.db.commit()
            return {"Message": "Tratamiento deleted successfully", "status": "deleted"}, 200
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}