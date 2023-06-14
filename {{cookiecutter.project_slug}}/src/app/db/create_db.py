import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.model import Base, Employee

engine = create_engine('sqlite:///employee.db')

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)