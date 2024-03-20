from sqlalchemy import Column, String
from src.Database.MySQL import Base


class MySQLPisosModel(Base):
    __tablename__ = 'floors'
    uuid = Column(String(36), primary_key=True)
    level = Column(String(36), nullable=False)
