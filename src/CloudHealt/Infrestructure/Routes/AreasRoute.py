# Importaciones de librería (descargadas)
from flask import request, Blueprint
from src.Database.MySQL import session_local

# Importaciones de aplicaciones (implementadas)
from src.CloudHealt.Infrestructure.Models.MySQLAreasModel import MySQLAreasModel

DataRoutes = Blueprint("/areas", __name__)

#Crear area
@DataRoutes.route('/area/crear', methods=['POST'])
def habitacionesCrear():        
    data : object = request.json
    
    print(data)
    
    new_habitacion = MySQLAreasModel(
        number = data.get('number'),
        area_uuid = data.get('area_uuid')
    )
    
    session_local.add(new_habitacion)
    session_local.commit()
    
    return {"status":200,"message":"Habitación creada"}, 200