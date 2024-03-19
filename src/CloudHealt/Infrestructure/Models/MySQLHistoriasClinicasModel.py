from sqlalchemy import Column, String, Integer, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, backref
from src.Database.MySQL import Base


class MySQLHistoriasClinicas(Base):
    __tablename__ = 'historiasclinicas'
    uuid = Column(String(36), primary_key=True)
    profesion = Column(String(255), nullable=False)
    weight = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
