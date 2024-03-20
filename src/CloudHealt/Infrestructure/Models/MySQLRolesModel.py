from sqlalchemy import Column, String
from src.Database.MySQL import Base


class MySQLRolesModel(Base):
    __tablename__ = 'roles'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
