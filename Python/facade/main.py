from .BookingTravelFacade import BookingTravelFacade
from .Trip import Trip

bookingTravelFacade = BookingTravelFacade()
trip = Trip()
trip.set_flight_departure("Paris")
trip.set_flight_destination("New York")
trip.set_flight_date("2025-01-01")
trip.set_roomId("123")
trip.set_check_in_date("2025-01-01")
trip.set_check_out_date("2025-01-05")
trip.set_car_rental_location("Paris")
trip.set_car_rental_start_date("2025-01-01")
trip.set_car_rental_end_date("2025-01-05")
trip.set_payment_method("visa")
trip.set_amount(1000)
bookingTravelFacade.book_trip(trip)
