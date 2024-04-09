# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLTratamientosModel import MySQLTratamientosModel

DataRoutes = Blueprint("tratamientos_routes", __name__)

#Listar tratamientos
@DataRoutes.route('/listar', methods=['GET'])
def tratamientosListar():        
    
    tratamientos = session_local.query(MySQLTratamientosModel).all()
    
    print("Listar tratamientos")
    print(tratamientos)
    
    arrayTratamientos = []
    arrayTratamientos = [{
        "uuid": tratamientos.uuid,
        "title": tratamientos.title,
        "description": tratamientos.description,
        "paciente_uuid": tratamientos.paciente_uuid        
    } for tratamientos in tratamientos]
       
    return {"status":200,"tratamientos":arrayTratamientos}, 200

#Obtener tratamientos por Id
@DataRoutes.route('/<uuid>', methods=['GET'])
def tratamientosPorUUID(uuid):
    tratamientos = session_local.query(MySQLTratamientosModel).filter_by(uuid=uuid).first()
    
    if tratamientos:        
        obj_tratamientos = {
            "uuid": tratamientos.uuid,
            "title": tratamientos.title,
            "description": tratamientos.description,
            "paciente_uuid": tratamientos.paciente_uuid      
        }
        session_local.commit()
        return {"status": 200,"message": "Habitación encontrada", "habitacion":obj_tratamientos }, 200
    else:
        return {"status": 404, "message": "Habitación no encontrada","habitacion":{}}, 404

#Crear tratamientos
@DataRoutes.route('/crear', methods=['POST'])
def tratamientosCrear():        
    data : object = request.json
    
    print(data)
    
    new_tratamientos= MySQLTratamientosModel(
        title = data.get('number'),
        description = data.get('area_uuid'),
        paciente_uuid = data.get('paciente_uuid')
    )
    
    session_local.add(new_tratamientos)
    session_local.commit()
    
    return {"status": 200, "message": "tratamiento creado"}, 200

# Actualizar tratamientos por UUID
@DataRoutes.route('/actualizar/<string:uuid>', methods=['PUT'])
def tratamientosActualizar(uuid):
    data : object = request.json
    
    # Verificar si la tratamientos existe
    existing_tratamientos = session_local.query(MySQLTratamientosModel).filter_by(uuid=uuid).first()
    if not existing_tratamientos:
        return {"status": 404, "message": "El tratamienton no existe"}, 404
    
    # Actualizar la habitación
    existing_tratamientos.title = data.get('title', existing_tratamientos.title)
    existing_tratamientos.description = data.get('description', existing_tratamientos.description)
    existing_tratamientos.paciente_uuid = data.get('paciente_uuid', existing_tratamientos.paciente_uuid)
    
    session_local.commit()
    
    return {"status": 200, "message": "Tratamiento actualizado correctamente"}, 200

    
#Eliminar tratamiento
@DataRoutes.route('/eliminar/<uuid>', methods=['DELETE'])
def tratamientoEliminar(uuid):
    tratamiento = session_local.query(MySQLTratamientosModel).filter_by(uuid=uuid).first()
    
    if tratamiento:
        session_local.delete(tratamiento)
        session_local.commit()
        return {"status": 200, "message": "tratamiento eliminado"}, 200
    else:
        return {"status": 404, "message": "tratamientos no encontrado"}, 404