from sqlalchemy import Column, String, Float
from src.Database.MySQL import Base
from uuid import uuid4

class MySQLHistoriasClinicas(Base):
    __tablename__ = 'historiasclinicas'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    profesion = Column(String(255), nullable=False)
    weight = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
