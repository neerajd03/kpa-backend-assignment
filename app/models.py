from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True)
    submitted_by = Column(String)
    submitted_date = Column(String)
    fields = Column(JSON)
