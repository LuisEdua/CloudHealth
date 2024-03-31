# Si estas en windows usar la terminal de Git Bash

# Crea el entorno 
python -m venv .venv 

# Entra en el entorno
source env/scripts/activate 

# Instala las dependencias dentro del entorno
pip install -r requirements.txt 

# Ejecuta la api dentro del entorno
python app.py

# Se sale del entorno
deactivate