# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLQuirofanosModel import MySQLQuirofanos

DataRoutes = Blueprint("/quirofano", __name__)

#Crear Quirofano
@DataRoutes.route('/quirofano/crear', methods=['POST'])
def quirofanoCrear():        
    data : object = request.json
    
    print(data)
    
    # Verificar si el número de habitación ya existe
    #existing_habitacion = session_local.query(MySQLQuirofanosModel).filter_by(number=data.get('number')).first()
    #if existing_habitacion:
    #    return {"status": 400, "message": "Ya existe una habitación con ese número"}, 400
    
    new_quirofano = MySQLQuirofanos(
        number = data.get("number"),
        description = data.get('description'),
        floor_uuid = data.get('floor_uuid'),
        paciente_uuid = data.get('paciente_uuid')
    )
    
    session_local.add(new_quirofano)
    session_local.commit()
    
    return {"status": 200, "message": "Quirofano creada"}, 200

#Listar Quirofano
@DataRoutes.route('/quirofano/listar', methods=['GET'])
def quirofanosListar():        
    
    print("====================Listar Quirofanos====================")

    quirofanos = session_local.query(MySQLQuirofanos).all()
    
    print(quirofanos)
    
    arrayQuirofanos = []
    arrayQuirofanos = [{
        "uuid": quirofano.uuid,
        "number": quirofano.number,
        "floor_uuid": quirofano.floor_uuid,
        "paciente_uuid": quirofano.paciente_uuid

    } for quirofano in quirofanos]
       
    return {"status":200,"quirofanos":arrayQuirofanos}, 200

#Obtener Quirofano por Id
@DataRoutes.route('/quirofano/<uuid>', methods=['GET'])
def habitacionesPorUUID(uuid):
    quirofano = session_local.query(MySQLQuirofanos).filter_by(uuid=uuid).first()
    
    if quirofano:        
        obj_abitacion = {
            "uuid": quirofano.uuid,
            "number": quirofano.number,
            "floor_uuid": quirofano.floor_uuid,
            "paciente_uuid": quirofano.paciente_uuid
        }
        session_local.commit()
        return {"status": 200,"message": "Quirofano encontrado", "Quirofano":obj_abitacion }, 200
    else:
        return {"status": 404, "message": "Quirofano no encontrado","Quirofano":{}}, 404



# Actualizar Quirofano por UUID
@DataRoutes.route('/quirofano/actualizar/<string:uuid>', methods=['PUT'])
def QuirofanoActualizar(uuid):
    data : object = request.json
    
    # Verificar si el Quirofano existe
    existing_quirofano = session_local.query(MySQLQuirofanos).filter_by(uuid=uuid).first()
    if not existing_quirofano:
        return {"status": 404, "message": "El quirofano no existe no existe"}, 404
    
    # Actualizar la Quirofano
    existing_quirofano.number = data.get('number', existing_quirofano.number)
    existing_quirofano.description = data.get('description', existing_quirofano.description)
    existing_quirofano.floor_uuid = data.get('floor_uuid', existing_quirofano.floor_uuid)
    existing_quirofano.paciente_uuid = data.get('description', existing_quirofano.description)
    
    session_local.commit()
    
    return {"status": 200, "message": "Quirofano actualizada correctamente"}, 200

    
#Eliminar Quirofano
@DataRoutes.route('/quirofano/eliminar/<uuid>', methods=['DELETE'])
def quirofanoEliminar(uuid):
    quirofano = session_local.query(MySQLQuirofanos).filter_by(uuid=uuid).first()
    
    if quirofano:
        session_local.delete(quirofano)
        session_local.commit()
        return {"status": 200, "message": "Quirofano eliminada"}, 200
    else:
        return {"status": 404, "message": "Quirofano no encontrada"}, 404