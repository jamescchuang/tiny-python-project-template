from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    position = Column(String(50))

    def __repr__(self):
        return "<Employee(name='%s', age='%s', position='%s')>" % (
                            self.name, self.age, self.position)