from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URL = 'mysql+pymysql://root:@127.0.0.1:3306/BDH'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
session_local = sessionmaker(bind=engine)
