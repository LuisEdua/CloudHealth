from src.CloudHealt.Domain.Ports.UsersPort import UsersPort
from src.CloudHealt.Domain.Entity.Users import Users
from src.CloudHealt.Infrestructure.Models.MySQLUsersModel import MySQLUsersModel as Model
from src.Database.MySQL import session_local, Base, engine
from src.CloudHealt.Infrestructure.MiddleWares.UsersMiddleWares import encrypt_password, verify_password
from src.CloudHealt.Infrestructure.MiddleWares.functionJWT import write_token
from flask import jsonify


class MySQLUsuariosRepository(UsersPort):

    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_users(self):
        try:
            users = self.db.query(Model).all()
            if users:
                return {"Message": "Users found successfully", "Users": [user.to_json() for user in users],
                        "status": "Success"}, 200
            else:
                return {"Message": "Users not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f'Something went wrong: \n {e}', 'status': 'error'}, 500

    def get_users_by_area(self, area_uuid):
        try:
            users = self.db.query(Model).filter(Model.area_uuid == area_uuid).all()
            if users:
                return {"Message": "Users found successfully", "Users": [user.to_json() for user in users],
                        "status": "Success"}, 200
            else:
                return {"Message": "Users not found", "status": "not found"}, 404
        except Exception as e:
            return {"Message": f'Something went wrong: \n{e}', "status": "error"}, 500

    def login(self, email: str, password: str):
        try:
            user = self.db.query(Model).filter(Model.email == email).first()
            if user:
                if verify_password(password, user.password):
                    token = write_token(data={"user_id": str(user.uuid)})
                    return {"Message": "User logged in", "token": f"{token}", "user": user.to_json(),
                            "status": "success"}, 200
                else:
                    return {"Message": "Invalid Password", "status": "unauthorized"}, 401
            else:
                return {"Message": "Invalid Email", "status": "unauthorized"}, 401
        except Exception as e:
            return {"Message": f'Something went wrong: \n{e}', "status": "error"}, 500

    def create(self, user: Users):
        try:
            pwd = encrypt_password(user.password)
            new = Model(uuid=user.uuid, firstname=user.firstname, lastname=user.lastname, age=user.age,
                        birthday=user.birthday, email=user.email, password=pwd, rol_uuid=user.role_uuid,
                        area_uuid=user.area_uuid)
            self.db.add(new)
            self.db.commit()
            return {"Message": "User created", "status": "success", "user": new.to_json()}, 201
        except Exception as e:
            return {"Message": f'Something went wrong: \n{e}', "status": "error"}, 500

    def update_user(self, uuid: str, email=None, password=None, area_uuid=None):
        try:
            user = self.db.query(Model).filter(Model.uuid == uuid).first()
            if user:
                user.email = email if email else user.email
                user.password = encrypt_password(password) if password else user.password
                user.area_uuid = area_uuid if area_uuid else user.area_uuid
                self.db.commit()
                return {"Message": "User updated", "status": "success", "user": user.to_json()}, 200
            else:
                return {"Message": "User not found", "status": "error"}, 404
        except Exception as e:
            return {"Message": f"Something went wrong: \n{e}", "status": "error"}, 500

    def delete_user(self, uuid: str):
        try:
            user = self.db.query(Model).filter(Model.uuid == uuid).first()
            if user:
                self.db.delete(user)
                self.db.commit()
                return jsonify({"Message": "User deleted successfully", "status": "success"}), 200
            else:
                return jsonify({"Message": "User not found", "status": "not found"}), 404
        except Exception as e:
            return jsonify({"Message": f"Something went wrong: \n{e}", "status": "error"}), 500
