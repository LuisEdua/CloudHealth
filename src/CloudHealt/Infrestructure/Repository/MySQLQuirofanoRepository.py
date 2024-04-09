from src.CloudHealt.Domain.Ports.QuirofanosPort import QuirofanosPort
from src.CloudHealt.Domain.Entity.Quirofanos import Quirofanos
from src.CloudHealt.Infrestructure.Models.MySQLQuirofanosModel import MySQLQuirofanosModel as Model
from src.Database.MySQL import Base, session_local, engine


class MySQLQuirofanoRepository(QuirofanosPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_all_quirofanos(self):
        try:
            quirofanos = self.db.query(Model).all()
            if quirofanos:
                return {"message": "Quirofanos found", "quirofanos": [q.to_json() for q in quirofanos],
                        "status": "Success"}, 200
            else:
                return {"message": "Quirofanos not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def get_quirofanos(self, floor_uuid):
        try:
            quirofanos = self.db.query(Model).filter(Model.floor_uuid == floor_uuid).all()
            if quirofanos:
                return {"message": "Quirofanos found", "quirofanos": [q.to_json() for q in quirofanos],
                        "status": "Success"}, 200
            else:
                return {"message": "Quirofanos not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500


    def create_quirofanos(self, quirofano: Quirofanos):
        try:
            new = Model(uuid = quirofano.uuid, number=quirofano.number, description=quirofano.description,
                        floor_uuid=quirofano.floor_uuid)
            self.db.add(new)
            self.db.commit()
            return {"message": "Quirofano created successfully", "quirofano": new.to_json(), "status": "success"}, 201
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
