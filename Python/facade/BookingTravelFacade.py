from .Trip import Trip
from .FlightManager import FlightManager
from .HotelReservation import HotelReservation
from .CarRental import CarRental
from .PaymentProcessor import PaymentProcessor
from .PaymentMethodFactory import PaymentMethodFactory

class BookingTravelFacade:
    def __init__(self):
        self.flightManager = FlightManager()
        self.hotelReservation = HotelReservation()
        self.carRental = CarRental()
        self.paymentProcessor = PaymentProcessor()
        self.paymentMethodFactory = PaymentMethodFactory()
    
    def book_trip(self, trip: Trip):
        paymentMethod = self.paymentMethodFactory.create_payment_method(trip.payment_method)
        
        self.flightManager.book_flight(trip.flight_departure, trip.flight_destination, trip.flight_date)
        self.hotelReservation.book_hotel(trip.roomId, trip.check_in_date, trip.check_out_date)
        self.carRental.book_car(trip.car_rental_location, trip.car_rental_start_date, trip.car_rental_end_date)
        self.paymentProcessor.process_payment(paymentMethod, trip.amount)



