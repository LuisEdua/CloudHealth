from src.CloudHealt.Domain.Ports.DiagnosticoPort import DiagnosticoPort
from src.CloudHealt.Domain.Entity.Diagnosticos import Diagnosticos
from src.CloudHealt.Infrestructure.Models.MySQLDiagnosticosModel import MySQLDiagnosticosModel as Model
from src.Database.MySQL import Base, engine, session_local


class MySQLDiagnosticoRepository(DiagnosticoPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_diagnosticos(self, paciente_uuid):
        try:
            diagnosticos = self.db.query(Model).filter(Model.paciente_uuid == paciente_uuid).all()
            if diagnosticos:
                return {"Message": "Diagnosticos encontrados",
                        "Diagnosticos":[diagnostico.to_json() for diagnostico in diagnosticos],
                        "status": "Success"}, 200
            else:
                return {"Message": "Diaganosticos not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500


    def create_diagnostico(self, diagnostico: Diagnosticos):
        try:
            new = Model(uuid=diagnostico.uuid, title=diagnostico.title, description=diagnostico.description,
                        paciente_uuid=diagnostico.paciente_uuid)
            self.db.add(new)
            self.db.commit()
            return {"Message": "Diagnostico created successfully", "Diagnostico": new.to_json(),
                    "status": "success"}, 201
        except Exception as e:
            return {"Message": f"Error: {e}", "status":"error"}, 500

    def update_diagnostico(self, uuid, title: str, description: str):
        try:
            diagnostico = self.db.query(Model).filter_by(uuid=uuid).first()
            if diagnostico:
                diagnostico.title = title
                diagnostico.description = description
                self.db.commit()
                return {"Message": "Diagnostico updated successfully", "diagnostico":diagnostico.to_json(),
                        "status": "success"}, 200
            else:
                return {"Message": "Diagnostico not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500

    def delete_diagnostico(self, uuid: str):
        try:
            diagnostico = self.db.query(Model).filter(Model.uuid == uuid).first()
            if diagnostico:
                self.db.delete(diagnostico)
                return {"Message": "Diagnostico deleted succesfully", "status": "success"}, 200
            else:
                return {"Message": "Diagnostico not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f"Error: {e}", "status": "error"}, 500
