#import unittest
from sqlalchemy.exc import IntegrityError
from flask import request, Blueprint
from src.Database.MySQL import session_local
from src.CloudHealt.Infrestructure.Models.MySQLUsersModel import MySQLUsersModel
from src.CloudHealt.Infrestructure.MiddleWares.UsersMiddleWares import encrypt_password
from sqlalchemy.exc import IntegrityError

DataRoutes = Blueprint("users_routes", __name__)

@DataRoutes.route('/list', methods=['GET'])
def list_users():    

    print("=================Listando Usuarios=============")

    usuarios = session_local.query(MySQLUsersModel).all()
    
    arrayUsuario = []
    arrayUsuario = [{
        "uuid": usuario.uuid,
        "firstname": usuario.firstname,
        "lastname": usuario.lastname,
        "age": usuario.age,
        "birthday": usuario.birthday ,
        "email": usuario.email,
        "password": usuario.password,  
        "rol_uuid": usuario.rol_uuid,
        "area_uuid": usuario.area_uuid,        
    } for usuario in usuarios]
       
    return {"status":200,"usuarios":arrayUsuario}, 200



@DataRoutes.route('/create', methods=['POST'])
def create_usuer():
    try:
        data = request.json

        # Crear una nueva instancia del modelo de usuario con los datos recibidos
        new_user = MySQLUsersModel(
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            age=data.get('age'),
            birthday=data.get('birthday'),
            email=data.get('email'),
            password=encrypt_password(data.get('password')),
            rol_uuid=data.get('rol_uuid'),
            area_uuid=data.get('area_uuid')
        )

        session_local.add(new_user)
        session_local.commit()
        return {"status": 200, "message": "Usuario creado correctamente"}, 200
    except IntegrityError as e:
        # Captura la excepción específica de integridad (clave duplicada)
        session_local.rollback()  # Revierte cualquier cambio pendiente en la sesión
        return {"status": 400, "message": "El correo electrónico ya está en uso"}, 400
    except Exception as e:
        # Captura cualquier otro tipo de excepción no esperada
        return {"status": 500, "message": "Error interno del servidor"}, 500