import hashlib

def encrypt_password(password):
    # Utilizamos el algoritmo SHA-256 para generar el hash de la contraseña
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def verify_password(input_password, hashed_password):
    # Comparamos el hash de la contraseña almacenada con el hash de la contraseña ingresada
    return hashed_password == hashlib.sha256(input_password.encode()).hexdigest()

