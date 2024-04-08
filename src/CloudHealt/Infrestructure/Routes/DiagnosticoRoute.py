# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLDiagnosticosModel import MySQLDiagnosticosModel


DataRoutes = Blueprint("/diagnostico", __name__)

#Crear diagnostico
@DataRoutes.route('/diagnostico/crear', methods=['POST'])
def diagnosticoCrear():
    data = request.json
    
    print(data)

    # Verificar si el número de diagnostico ya existe
    #existing_area = session_local.query(MySQLDiagnosticosModel).filter_by(name=data.get('name')).first()
    #if existing_area:
    #    return {"status": 400, "message": "Ya existe un diagnostico con ese número"}, 400
    
    new_diagnostico = MySQLDiagnosticosModel(        
        title = data.get('title'),
        description = data.get('description'),
        paciente_uuid = data.get('paciente_uuid')
    )
    print("pss")
    session_local.add(new_diagnostico)
    session_local.commit()
    
    return {"status": 200, "message": "diagnostico creado"}, 200

#Listar diagnosticos
@DataRoutes.route('/diagnostico/listar', methods=['GET'])
def diagnosticoListar():        
    
    areas = session_local.query(MySQLDiagnosticosModel).all()
    
    print("Listar diagnosticos")
    print(diagnostico)
    
    arrayDiagnostico = []
    arrayDiagnostico = [{
        "uuid": diagnosticos.uuid,
        "title": diagnosticos.title,
        "description": description.description,        
        "paciente_uuid": description.paciente_uuid        


    } for diagnostico in diagnostico]
       
    return {"status":200,"diagnosticos":arrayDiagnostico}, 200

#Obtener diagnosticos por Id
@DataRoutes.route('/diagnosticos/<uuid>', methods=['GET'])
def diagnosticoPorUUID(uuid):
    diagnostico = session_local.query(MySQLDiagnosticosModel).filter_by(uuid=uuid).first()
    
    if diagnostico:        
        obj_area = {
            "uuid": diagnosticos.uuid,
            "title": diagnosticos.title,
            "description": description.description,        
            "paciente_uuid": description.paciente_uuid
        }
        session_local.commit()
        return {"status": 200,"message": "Diagnosticos encontrado", "diagnosticos":obj_area }, 200
    else:
        return {"status": 404, "message": "diagnosticos no encontrada","diagnosticos":{}}, 404

# Actualizar diagnosticos por UUID
@DataRoutes.route('/diagnosticos/actualizar/<string:uuid>', methods=['PUT'])
def diagnosticosActualizar(uuid):
    data : object = request.json
    
    # Verificar si la area existe
    existing_diagnosticos = session_local.query(MySQLDiagnosticosModel).filter_by(uuid=uuid).first()
    if not existing_diagnosticos:
        return {"status": 404, "message": "El diagnosticos no existe"}, 404
    
    # Actualizar la area
    existing_diagnosticos.title = data.get('title', existing_diagnosticos.title)
    existing_diagnosticos.description = data.get('description', existing_diagnosticos.description)
    existing_diagnosticos.paciente_uuid = data.get('paciente_uuid', existing_diagnosticos.paciente_uuid)

    session_local.commit()
    
    return {"status": 200, "message": "Diagnosticos actualizado correctamente"}, 200

#Eliminar diagnosticos
@DataRoutes.route('/diagnosticos/eliminar/<uuid>', methods=['DELETE'])
def diagnosticosEliminar(uuid):
    diagnosticos = session_local.query(MySQLDiagnosticosModel).filter_by(uuid=uuid).first()
    
    if diagnosticos:
        session_local.delete(diagnosticos)
        session_local.commit()
        return {"status": 200, "message": "Diagnosticos eliminado"}, 200
    else:
        return {"status": 404, "message": "Diagnosticos no encontrada"}, 404