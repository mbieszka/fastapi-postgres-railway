from sqlalchemy import Column, Integer, Float, Date
from db import Base

class EnergyPrice(Base):
    __tablename__ = "energy_prices"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True)
    price = Column(Float)
