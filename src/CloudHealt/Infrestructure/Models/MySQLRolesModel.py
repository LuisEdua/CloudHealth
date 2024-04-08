from sqlalchemy import Column, String
from src.Database.MySQL import Base
from uuid import uuid4
from uuid import uuid4
class MySQLRolesModel(Base):
    __tablename__ = 'roles'
    uuid = Column(String(36), primary_key=True, default=uuid4())
    name = Column(String(100), nullable=False)
