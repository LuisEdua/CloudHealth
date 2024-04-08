# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLDeportesModel import MySQLDeportesModel

DataRoutes = Blueprint("/deportes", __name__)

#Listar Deportes
@DataRoutes.route('/deportes/listar', methods=['GET'])
def deportesListar():        
    
    deportes = session_local.query(MySQLDeportesModel).all()
    
    print("Listar deportes")
    print(deportes)
    
    arrayDeportes = []
    arrayDeportes = [{
        "uuid": deportes.uuid,
        "name": deportes.name,
        "historia_uuid": deportes.number,    
    } for deportes in deportes]
       
    return {"status":200,"deportes":arrayDeportes}, 200

#Obtener deportes por Id
@DataRoutes.route('/deportes/<uuid>', methods=['GET'])
def deportesPorUUID(uuid):
    deportes = session_local.query(MySQLDeportesModel).filter_by(uuid=uuid).first()
    
    if deportes:        
        obj_deportes = {
        "uuid": deportes.uuid,
        "name": deportes.name,
        "historia_uuid": deportes.number, 
        }
        session_local.commit()
        return {"status": 200,"message": "deportes encontrado", "deportes":obj_deportes }, 200
    else:
        return {"status": 404, "message": "deportes no encontrado","deportes":{}}, 404

#Crear deportes
@DataRoutes.route('/deportes/crear', methods=['POST'])
def deportesCrear():        
    data : object = request.json
    
    print(data)
    
    new_deportes = MySQLDeportesModel(
        name = data.get('name'),
        historia_uuid = data.get('historia_uuid')
    )
    
    session_local.add(new_deportes)
    session_local.commit()
    
    return {"status": 200, "message": "Deporte creado"}, 200

# Actualizar Deporte por UUID
@DataRoutes.route('/deportes/actualizar/<string:uuid>', methods=['PUT'])
def deportesActualizar(uuid):
    data : object = request.json
    
    # Verificar si la habitación existe
    existing_deportes = session_local.query(MySQLDeportesModel).filter_by(uuid=uuid).first()
    if not existing_deportes:
        return {"status": 404, "message": "El deporte no existe"}, 404
    
    # Actualizar la habitación
    existing_deportes.name = data.get('name', existing_deportes.name)
    existing_deportes.historia_uuid = data.get('historia_uuid', existing_deportes.historia_uuid)
    
    
    session_local.commit()
    
    return {"status": 200, "message": "Deporte actualizado correctamente"}, 200

    
#Eliminar deportes
@DataRoutes.route('/deportes/eliminar/<uuid>', methods=['DELETE'])
def deportesEliminar(uuid):
    deportes = session_local.query(MySQLDeportesModel).filter_by(uuid=uuid).first()
    
    if deportes:
        session_local.delete(deportes)
        session_local.commit()
        return {"status": 200, "message": "deporte eliminado"}, 200
    else:
        return {"status": 404, "message": "deportes no encontrado"}, 404