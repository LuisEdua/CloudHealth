from src.CloudHealt.Domain.Entity.Lesiones import Lesiones
from src.CloudHealt.Domain.Ports.LessionesPort import LessionesPort
from src.Database.MySQL import Base, engine, session_local
from src.CloudHealt.Infrestructure.Models.MySQLLesionesModel import MySQLLesionesModel as Model


class MySQLLesionesRepository(LessionesPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_lesiones(self, historia_uuid):
        try:
            lesiones = self.db.query(Model).filter(Model.historia_uuid == historia_uuid).all()
            if lesiones:
                return  {"Message": "Lesiones found successfully", "status": "success",
                         "lesiones": [lesion.to_json() for lesion in lesiones]}, 200
            else:
                return {"Message": "Lessiones not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': 'error'}, 500

    def create_lesiones(self, lesiones: list[Lesiones]):
        try:
            news = []
            for lesion in lesiones:
                new = Model(uuid=lesion.uuid, title= lesion.title, description= lesion.description,
                            historia_uuid=lesion.historia_uuid)
                news.append(new)
            self.db.add_all(news)
            self.db.commit()
            return {"Message": "Lessiones added", "status": "success",
                    "lesiones": [new.to_json() for new in news]}, 201
        except Exception as e:
            return {"Message": f'Error: {e}', 'status': 'error'}, 500