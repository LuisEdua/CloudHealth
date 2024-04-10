from src.CloudHealt.Domain.Entity.Deportes import Deportes
from src.CloudHealt.Domain.Ports.DeportesPort import DeportesPort
from src.Database.MySQL import Base, session_local, engine
from src.CloudHealt.Infrestructure.Models.MySQLDeportesModel import MySQLDeportesModel as Model


class MySQLDeportesRepository(DeportesPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_deportes(self, historia_uuid):
        try:
            deportes = self.db.query(Model).filter(Model.historia_uuid == historia_uuid).all()
            if deportes:
                return {"Message": "Deportes found successfully", "status": "success",
                        "deportes": [deporte.to_json() for deporte in deportes]}, 200
            else:
                return {"Message": "Deportes not found", "status": "not found"},404
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': 'error'}, 500

    def create_deportes(self, deportes: list[Deportes]):
        try:
            news = []
            for deporte in deportes:
                new = Model(uuid=deporte.uuid, name=deporte.name, historia_uuid=deporte.historia_uuid)
                news.append(new)
            self.db.add_all(news)
            self.db.commit()
            return {"Message": "Deportes created successfully", "status": "Success",
                    "deportes": [new.to_json() for new in news]}, 201
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': 'error'}, 500
