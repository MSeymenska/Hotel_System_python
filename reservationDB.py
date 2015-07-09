from sqlalchemy import *
from base import Base
from sqlalchemy.orm import relationship

class ReservationDB(Base):
	__tablename__ = 'ReservationDB'
	EGN = Column(String, primary_key = True)
	first_name = Column(String)
	last_name = Column(String)
	room_number = Column(Integer)
	breakfast = Column(String)
	date_check_in = Column(Date)
	date_check_out = Column(Date)
	prize = Column(Integer)
	children = Column(String)
	room_number_s = relationship('Room', backref='ReservationDB.room_number')