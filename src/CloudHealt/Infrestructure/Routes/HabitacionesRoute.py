# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLHabitacionesModel import MySQLHabitacionesModel

DataRoutes = Blueprint("/habitaciones", __name__)

#Listar Habitaciones
@DataRoutes.route('/habitaciones/listar', methods=['GET'])
def habitacionesListar():        
    
    habitaciones = session_local.query(MySQLHabitacionesModel).all()
    
    print("Listar habitaciones")
    print(habitaciones)
    
    arrayHabitaciones = []
    arrayHabitaciones = [{
        "uuid": habitacion.uuid,
        "number": habitacion.number,
        "area_uuid": habitacion.area_uuid        
    } for habitacion in habitaciones]
       
    return {"status":200,"habitaciones":arrayHabitaciones}, 200

#Obtener Habitacion por Id
@DataRoutes.route('/habitaciones/<uuid>', methods=['GET'])
def habitacionesPorUUID(uuid):
    habitacion = session_local.query(MySQLHabitacionesModel).filter_by(uuid=uuid).first()
    
    if habitacion:        
        obj_abitacion = {
            "uuid": habitacion.uuid,
            "number": habitacion.number,
            "area_uuid": habitacion.area_uuid   
        }
        session_local.commit()
        return {"status": 200,"message": "Habitación encontrada", "habitacion":obj_abitacion }, 200
    else:
        return {"status": 404, "message": "Habitación no encontrada","habitacion":{}}, 404

#Crear Habitacion
@DataRoutes.route('/habitaciones/crear', methods=['POST'])
def habitacionesCrear():        
    data : object = request.json
    
    print(data)
    
    # Verificar si el número de habitación ya existe
    existing_habitacion = session_local.query(MySQLHabitacionesModel).filter_by(number=data.get('number')).first()
    if existing_habitacion:
        return {"status": 400, "message": "Ya existe una habitación con ese número"}, 400
    
    new_habitacion = MySQLHabitacionesModel(
        number = data.get('number'),
        area_uuid = data.get('area_uuid')
    )
    
    session_local.add(new_habitacion)
    session_local.commit()
    
    return {"status": 200, "message": "Habitación creada"}, 200

# Actualizar Habitacion por UUID
@DataRoutes.route('/habitaciones/actualizar/<string:uuid>', methods=['PUT'])
def habitacionesActualizar(uuid):
    data : object = request.json
    
    # Verificar si la habitación existe
    existing_habitacion = session_local.query(MySQLHabitacionesModel).filter_by(uuid=uuid).first()
    if not existing_habitacion:
        return {"status": 404, "message": "La habitación no existe"}, 404
    
    # Actualizar la habitación
    existing_habitacion.number = data.get('number', existing_habitacion.number)
    existing_habitacion.area_uuid = data.get('area_uuid', existing_habitacion.area_uuid)
    
    session_local.commit()
    
    return {"status": 200, "message": "Habitación actualizada correctamente"}, 200

    
#Eliminar Habitacion
@DataRoutes.route('/habitaciones/eliminar/<uuid>', methods=['DELETE'])
def habitacionesEliminar(uuid):
    habitacion = session_local.query(MySQLHabitacionesModel).filter_by(uuid=uuid).first()
    
    if habitacion:
        session_local.delete(habitacion)
        session_local.commit()
        return {"status": 200, "message": "Habitación eliminada"}, 200
    else:
        return {"status": 404, "message": "Habitación no encontrada"}, 404