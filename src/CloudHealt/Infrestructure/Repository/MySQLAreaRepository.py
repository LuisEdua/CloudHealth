from seaborn._marks.area import Area

from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel as Model
from src.CloudHealt.Domain.Ports.AreasPort import AreasPorts
from src.CloudHealt.Domain.Entity.Areas import Areas
from src.Database.MySQL import Base, engine, session_local


class MySQLAreaRepository(AreasPorts):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_areas_by_id(self, area_uuid):
        try:
            area = self.db.query(Model).filter(Model.uuid == area_uuid).first()
            if area:
                return {"message": "Area found", "area": area.to_json(), "status": "Success"}, 200
            else:
                return {"message": "Area not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def get_areas_by_floor(self, floor_uuid):
        try:
            areas = self.db.query(Model).filter(Model.floor_uuid == floor_uuid).all()
            if areas:
                return {"message": "Areas found", "areas": [a.to_json() for a in areas], "status": "Success"}, 200
            else:
                return {"message": "Areas not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def get_all_areas(self):
        try:
            areas = self.db.query(Model).all()
            if areas:
                return {"message": "Areas found", "areas": [a.to_json() for a in areas], "status": "Success"}, 200
            else:
                return {"message": "Areas not found", "status": "not found"}, 404
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500

    def create_area(self, area: Areas):
        try:
            new = Model(uuid=area.uuid, floor_uuid=area.floor_uuid, name=area.name)
            self.db.add(new)
            self.db.commit()
            return {"message": "area created successfully", "area": new.to_json(), "status": "Success"}, 201
        except Exception as e:
            return {"message": str(e), "status": "error"}, 500
