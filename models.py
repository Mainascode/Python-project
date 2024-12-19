# models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import DATABASE_URI

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Store hashed passwords
    clients = relationship("Client", back_populates="user")

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    income = Column(Float)
    expenses = Column(Float)
    savings = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id')) # Link to User table

    # Relationship with User
    user = relationship("User", back_populates="clients")
    investments = relationship("Investment", back_populates="client")

class Investment(Base):
    __tablename__ = 'investments'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    # Relationship with Client
    client = relationship("Client", back_populates="investments")

# Setup the database
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()