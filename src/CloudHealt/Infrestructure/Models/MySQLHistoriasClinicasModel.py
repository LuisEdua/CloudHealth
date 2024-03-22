from sqlalchemy import Column, String, Float
from src.Database.MySQL import Base


class MySQLHistoriasClinicas(Base):
    __tablename__ = 'historiasclinicas'
    uuid = Column(String(36), primary_key=True)
    profesion = Column(String(255), nullable=False)
    weight = Column(Float, nullable=False)
    high = Column(Float, nullable=False)

    def to_json(self):
        return {
            'uuid': self.uuid,
            'profesion': self.profesion,
            'weight': self.weight,
            'high': self.high
        }