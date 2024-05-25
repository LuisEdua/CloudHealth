from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DBUSER')
db_password = os.getenv('DBPASS')
db_url = os.getenv('DBURL')
db_name = os.getenv('DBNAME')

Base = declarative_base()

DATABASE_URL = f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}'
#DATABASE_URL = 'mysql+pymysql://root:RcBaR_-315@127.0.0.1:3306/BDH' #Luis
#DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/BDH' #Karla
#DATABASE_URL = 'mysql+pymysql://python.user:a12345678.@127.0.0.1:3306/bdh' #Simuta

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
session_local = sessionmaker(bind=engine)
