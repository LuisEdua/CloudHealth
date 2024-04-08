from flask import request, Blueprint, jsonify
from src.Database.MySQL import session_local
from src.CloudHealt.Infrestructure.Models.MySQLUsersModel import MySQLUsersModel
from src.CloudHealt.Infrestructure.MiddleWares.UsersMiddleWares import encrypt_password, verify_password
DataRoutes = Blueprint("/users", __name__)

@DataRoutes.route('/users/list', methods=['GET'])
def list_users():        
    usuarios = session_local.query(MySQLUsersModel).all()
    arrayUsuario = []
    arrayUsuario = [{
        "uuid": usuario.uuid,
        "firstname": usuario.firstname,
        "lastname": usuario.lastname,
        "age": usuario.age,
        "birthday": usuario.birthday.isoformat() if usuario.birthday else None,
        "email": usuario.email,
        "password": usuario.password,  
        "rol_uuid": usuario.rol_uuid,
        "area_uuid": usuario.area_uuid,
        # "area": usuario.area,
    } for usuario in usuarios]
       
    return {"status":200,"usuarios":arrayUsuario}, 200

@DataRoutes.route('/users/create', methods=['POST'])
def create_usuer():
    data = request.json
    print(verify_password('unaContraseñaSegura','eaf21a1037b332b84ea4c8bb461e295b19f10e123844f123ab63926e66d4f65d'))
    # Crear una nueva instancia del modelo de usuario con los datos recibidos
    new_user = MySQLUsersModel(
        firstname=data.get('firstname'),
        lastname=data.get('lastname'),
        age=data.get('age'),
        birthday=data.get('birthday'),
        email=data.get('email'),
        password=  encrypt_password(data.get('password')) ,
        rol_uuid=data.get('rol_uuid'),
        area_uuid=data.get('area_uuid')
    )
    session_local.add(new_user)
    session_local.commit()
    
    return {"status": 200, "message": "Usuario creado correctamente"}, 200