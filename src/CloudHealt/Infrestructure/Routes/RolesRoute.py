from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLRolesModel import MySQLRolesModel

DataRoutes = Blueprint("/roles", __name__)

#Listar roles
@DataRoutes.route('/roles/listar', methods=['GET'])
def hrolesListar():        
    
    roles = session_local.query(MySQLRolesModel).all()
    
    print("Listar roles")
    print(roles)
    
    arrayRoles = []
    arrayRoles = [{
        "uuid": roles.uuid,
        "name": roles.name,      
    } for roles in roles]
       
    return {"status":200,"roles":arrayRoles}, 200

#Obtener rol por Id
@DataRoutes.route('/roles/<uuid>', methods=['GET'])
def rolesPorUUID(uuid):
    roles = session_local.query(MySQLRolesModel).filter_by(uuid=uuid).first()
    
    if roles:        
        obj_roles = {
            "uuid": roles.uuid,
            "name": roles.name,  
        }
        session_local.commit()
        return {"status": 200,"message": "Rol encontrado", "Rol":obj_roles }, 200
    else:
        return {"status": 404, "message": "Rol no encontrado","Rol":{}}, 404

#Crear roles
@DataRoutes.route('/roles/crear', methods=['POST'])
def rolesCrear():        
    data : object = request.json
    
    print(data)
    
    # Verificar si el número de habitación ya existe
    existing_roles = session_local.query(MySQLRolesModel).filter_by(name=data.get('name')).first()
    if existing_roles:
        return {"status": 400, "message": "Ya existe un rol con ese nombre"}, 400
    
    new_rol = MySQLRolesModel(
        name = data.get('name')
    )
    
    session_local.add(new_rol)
    session_local.commit()
    
    return {"status": 200, "message": "Rol creada"}, 200

# Actualizar roles por UUID
@DataRoutes.route('/roles/actualizar/<string:uuid>', methods=['PUT'])
def rolesActualizar(uuid):
    data : object = request.json
    
    # Verificar si la habitación existe
    existing_roles = session_local.query(MySQLRolesModel).filter_by(uuid=uuid).first()
    if not existing_roles:
        return {"status": 404, "message": "El rol no existe"}, 404
    
    # Actualizar la habitación
    existing_roles.name = data.get('name', existing_roles.name)

    
    session_local.commit()
    
    return {"status": 200, "message": "Rol actualizado correctamente correctamente"}, 200

    
#Eliminar roles
@DataRoutes.route('/roles/eliminar/<uuid>', methods=['DELETE'])
def rolEliminar(uuid):
    rol = session_local.query(MySQLRolesModel).filter_by(uuid=uuid).first()
    
    if rol:
        session_local.delete(rol)
        session_local.commit()
        return {"status": 200, "message": "Rol eliminado"}, 200
    else:
        return {"status": 404, "message": "Rol no encontrado"}, 404