import cx_Oracle

#creates data base with the following attributes:(show the paper)
#First name, Last name, EGN, Room type, Prize for a night,Prize for breakfast, Number of Accomodators, Check-in date, Check-out date, Breakfast, Children

class HotelReservation(object):
	def __init__(self):
		pass

	def make_reservation(self):
		pass
		#creates Reservation object 
		#the method needs first_name, last_name, egn, room_type, number_of_accomodators, check-in_date, check-out_date
		#if information is given, breakfast reservation is written in the object attributes
		#the method returns the created object
	
	def cancel_reservation(self):
		pass
		#creates Reservation object 
		#the method needs first_name and last_name
		#the method returns the created object
		

	def check_availability(self):
		pass
		#clients can check the availability by filtering with room_type, check-in_date, check-out_date

	def __check(self):
		#makes verification for available rooms before confirming

	def __refresh_db(self):
		pass
		#the make_reservation and check_availability methods will use this one
		#the method will delete old room and restaurant reservations

	def __calculating_prise(self):
		pass
		#calculates the prise for the whole stay

	def __show_prize(self):
		pass
		#shows the clients the prize they'll have to pay before confirming the reservations

	def confirm_reservation(self):
		pass
		#the method uses the returned object from make_reservation and
		#writes the object's attributes in the data base
		#before writing checks if there are available rooms (__check method)

	def confirm_cancelation(self):
		pass
		#the method uses the returned object from cancel_reservation and
		#deletes the reservation from the data base
		#automatically cancels the restaurant reservation


class Reservation(object):
	def __init__(self):
		pass
		
#Reservation object will have the following attributes:
#first_name, last_name, egn, room_type, check-in_date, check-out_date, number_of_accomodators, children, breakfast

		