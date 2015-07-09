import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker


import base
import reservationDB
import roomDB
#creates data base with the following attributes:(show the paper)
#Firstname, Last name, EGN, Room type, Prize for a night,Prize for breakfast, Number of Accomodators, Check-in date, Check-out date, Breakfast, Children
engine = create_engine("sqlite:///:memory:")
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()



class HotelReservation(object):
	def __init__(self):
		pass

	def make_reservation(self, first_name, last_name, egn, room_type, checkin_date, checkout_date, children=False, breakfast=False):
		if children and not breakfast:
			reservation = Reservation(first_name,last_name, egn, room_type, checkin_date, checkout_date, True, False)
		if not children and breakfast:
			reservation = Reservation(first_name,last_name, egn, room_type, checkin_date, checkout_date, False, True)
		if not children and not breakfast:
			reservation = Reservation(first_name,last_name, egn, room_type, checkin_date, checkout_date, False, False)
		if children and breakfast:
			reservation = Reservation(first_name,last_name, egn, room_type, checkin_date, checkout_date, True, True)
		return reservation
		#creates Reservation object 
		#the method needs first_name, last_name, egn, room_type, check-in_date, check-out_date
		#if information is given, breakfast reservation is written in the object attributes
		#the method returns the created object

	def confirm_reservation(self, first_name, last_name, egn, room_type, checkin_date, checkout_date, children=False, breakfast=False):
		self.__refresh_db()
		room_number = self.__check(room_type, checkin_date, checkout_date)
		if room_number is not 0:
			reservation = self.make_reservation(first_name, last_name, egn, room_type, checkin_date, checkout_date, children, breakfast)
			res = reservationDB.ReservationDB()
			room = roomDB.Room()
			
			res.EGN = reservation.egn
			res.first_name = reservation.first_name
			res.last_name = reservation.last_name
			res.room_number = room_number
			res.breakfast = reservation.breakfast
			res.check_in_date = reservation.check_in_date
			res.check_out_date = reservation.check_out_date
			res.children = reservation.children
			res.prize = self.__calculating_prize(room_type, checkin_date, checkout_date)
			
			room.room_number = room_number
			room.room_type = room_type
			room.checkin_date = checkin_date
			room.checkout_date = checkout_date
			room.reservation_rnumber = room_number
			res.room_number_s.append(room)
			session.add(room)
			session.commit()
		else:
			print("No available rooms for this period")

		#the method uses the returned object from make_reservation and
		#writes the object's attributes in the data base
		#before writing checks if there are available rooms (__check method)
	
	def cancel_reservation(self, egn):
		reservation = Reservation(egn)
		return reservation
		#creates Reservation object 
		#the method needs egn
		#the method returns the created object

	def confirm_cancelation(self, egn):
		cancelation = self.cancel_reservation(egn)
#		cancel = session.query(ReservationDB).get(egn)
#		session.delete(cancel)
		#the method uses the returned object from cancel_reservation and
		#deletes the reservation from the data base
		#automatically cancels the restaurant reservation
		

	def check_availability(self):
		pass
		#clients can check the availability by filtering with room_type, check-in_date, check-out_date

	def __check(self, room_type, checkin_date, checkout_date):
		pass
		#makes verification for available rooms before confirming
		#returns room number, in case of no available rooms returns 0

	def __refresh_db(self):
		pass
		#the confirm_reservation and check_availability methods will use this one
		#the method will delete old room and restaurant reservations

	def __calculating_prize(self, room_type, checkin_date, checkout_date):
		pass
		#calculates the prise for the whole stay
		#returns the calculation


class Reservation(object):
	def __init__(self, egn, first_name=None, last_name=None, room_type=None, check_in_date=None, check_out_date=None, children=None, breakfast=None):
		self.first_name = first_name
		self.last_name = last_name
		self.egn = egn
		self.room_type = room_type
		self.check_in_date = check_in_date
		self.check_out_date = check_out_date
		self.children = children
		self.breakfast = breakfast
		
#Reservation object will have the following attributes:
#first_name, last_name, egn, room_type, check-in_date, check-out_date, children, breakfast

		
