from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class Medicine(Base):
    __tablename__ = 'medicines'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    expiry_date = Column(Date)
    available = Column(Boolean)

    def __repr__(self):
        return f"<Medicine(name='{self.name}', category='{self.category}', quantity='{self.quantity}', expiry_date='{self.expiry_date}', available='{self.available}')>"

    def mark_as_available(self):
        self.available = True

    def mark_as_unavailable(self):
        self.available = False

    def is_expired(self):
        return self.expiry_date < date.today()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)

engine = create_engine('sqlite:///medicine.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
