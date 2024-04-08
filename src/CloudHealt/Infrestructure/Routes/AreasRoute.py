# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel


DataRoutes = Blueprint("/areas", __name__)

#Crear Area
@DataRoutes.route('/area/crear', methods=['POST'])
def areaCrear():        
    data = request.json
    
    print(data)

    # Verificar si el número de habitación ya existe
    existing_area = session_local.query(MySQLAreasModel).filter_by(name=data.get('name')).first()
    if existing_area:
        return {"status": 400, "message": "Ya existe una area con ese número"}, 400
    
    new_habitacion = MySQLAreasModel(
        name = data.get('name'),
        floor_uuid = data.get('floor_uuid')
    )
    
    session_local.add(new_habitacion)
    session_local.commit()
    
    return {"status": 200, "message": "Area creada"}, 200

#Listar areas
@DataRoutes.route('/areas/listar', methods=['GET'])
def areasListar():        
    
    areas = session_local.query(MySQLAreasModel).all()
    
    print("Listar Areas")
    print(areas)
    
    arrayAreas = []
    arrayAreas = [{
        "uuid": area.uuid,
        "name": area.name,
        "floor_uuid": area.floor_uuid        
    } for area in areas]
       
    return {"status":200,"areas":arrayAreas}, 200

#Obtener Habitacion por Id
@DataRoutes.route('/areas/<uuid>', methods=['GET'])
def areasPorUUID(uuid):
    area = session_local.query(MySQLAreasModel).filter_by(uuid=uuid).first()
    
    if area:        
        obj_area = {
            "uuid": area.uuid,
            "name": area.name,
            "floor_uuid": area.floor_uuid
        }
        session_local.commit()
        return {"status": 200,"message": "Area encontrada", "habitacion":obj_area }, 200
    else:
        return {"status": 404, "message": "Area no encontrada","habitacion":{}}, 404

# Actualizar Area por UUID
@DataRoutes.route('/area/actualizar/<string:uuid>', methods=['PUT'])
def areaActualizar(uuid):
    data : object = request.json
    
    # Verificar si la area existe
    existing_area = session_local.query(MySQLAreasModel).filter_by(uuid=uuid).first()
    if not existing_area:
        return {"status": 404, "message": "La Area no existe"}, 404
    
    # Actualizar la area
    existing_area.name = data.get('name', existing_area.name)
    existing_area.floor_uuid = data.get('floor_uuid', existing_area.floor_uuid)
    
    session_local.commit()
    
    return {"status": 200, "message": "Area actualizada correctamente"}, 200

#Eliminar Area
@DataRoutes.route('/area/eliminar/<uuid>', methods=['DELETE'])
def areaEliminar(uuid):
    area = session_local.query(MySQLAreasModel).filter_by(uuid=uuid).first()
    
    if area:
        session_local.delete(area)
        session_local.commit()
        return {"status": 200, "message": "Area eliminada"}, 200
    else:
        return {"status": 404, "message": "Area no encontrada"}, 404