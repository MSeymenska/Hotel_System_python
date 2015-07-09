from sqlalchemy import *
from base import Base
import reservationDB

class Room(Base):
	__tablename__ = 'Room'
	room_number = Column(Integer, primary_key = True)
	room_type = Column(String)
	checkin_date = Column(Date)
	checkout_date = Column(Date)
	reservation_rnumber = Column(Integer, ForeignKey('ReservationDB.room_number'))