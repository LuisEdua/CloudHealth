from sqlalchemy import Column, String
from src.Database.MySQL import Base
from uuid import uuid4

class MySQLPisosModel(Base):
    __tablename__ = 'floor'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    level = Column(String(255), nullable=False)
