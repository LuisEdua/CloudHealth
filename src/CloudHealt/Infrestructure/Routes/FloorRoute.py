# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLPisosModel import MySQLPisosModel


DataRoutes = Blueprint("/piso", __name__)

#Crear Piso
@DataRoutes.route('/piso/crear', methods=['POST'])
def pisoCrear():        

    data = request.json
    
    print(data)

    # Verificar si el número de habitación ya existe
    existing_piso = session_local.query(MySQLPisosModel).filter_by(level=data.get('level')).first()
    if existing_piso:
        return {"status": 400, "message": "Ya existe una piso con ese nivel"}, 400
    
    print("Creando piso")
    new_piso = MySQLPisosModel(
        level = data.get('level'),
    )
    
    print("Agregando el piso")
    session_local.add(new_piso)
    session_local.commit()
    
    return {"status": 200, "message": "Piso creado"}, 200

#Listar Piso
@DataRoutes.route('/piso/listar', methods=['GET'])
def pisoListar():        
    
    pisos = session_local.query(MySQLPisosModel).all()
    
    print("Listar Areas")
    print(pisos)
    
    arrayPisoss = []
    arrayPisoss = [{
        "uuid": piso.uuid,
        "level": piso.level
             
    } for piso in pisos]
       
    return {"status":200,"pisos":arrayPisoss}, 200

#Obtener Piso por Id
@DataRoutes.route('/piso/<uuid>', methods=['GET'])
def pisoPorUUID(uuid):
    piso = session_local.query(MySQLPisosModel).filter_by(uuid=uuid).first()
    
    if piso:        
        obj_piso= {
            "level": piso.level
        }
        session_local.commit()
        return {"status": 200,"message": "piso encontrado", "pisos":obj_piso }, 200
    else:
        return {"status": 404, "message": "piso no encontrado"}, 404

# Actualizar Piso por UUID
@DataRoutes.route('/piso/actualizar/<string:uuid>', methods=['PUT'])
def pisoActualizar(uuid):
    data : object = request.json
    
    # Verificar si la piso existe
    existing_piso = session_local.query(MySQLPisosModel).filter_by(uuid=uuid).first()
    if not existing_piso:
        return {"status": 404, "message": "La Area no existe"}, 404
    
    # Actualizar la area
    existing_piso.level = data.get('level', existing_piso.level)
    
    session_local.commit()
    
    return {"status": 200, "message": "Piso actualizado correctamente"}, 200

#Eliminar Piso
@DataRoutes.route('/piso/eliminar/<uuid>', methods=['DELETE'])
def pisoEliminar(uuid):
    piso = session_local.query(MySQLPisosModel).filter_by(uuid=uuid).first()
    
    if piso:
        session_local.delete(piso)
        session_local.commit()
        return {"status": 200, "message": "Piso eliminada"}, 200
    else:
        return {"status": 404, "message": "Piso no encontrada"}, 404