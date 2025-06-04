class Trip:
    def __init__(
            self, 
            flight_departure: str, 
            flight_destination: str, 
            flight_date: str, 
            roomId: str, 
            check_in_date: str, 
            check_out_date: str,
            car_rental_location: str,
            car_rental_start_date: str,
            car_rental_end_date: str,
            payment_method: str,
            amount: float
            ):
        
        self.flight_departure = flight_departure
        self.flight_destination = flight_destination
        self.flight_date = flight_date
        self.roomId = roomId
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.car_rental_location = car_rental_location
        self.car_rental_start_date = car_rental_start_date
        self.car_rental_end_date = car_rental_end_date
        self.payment_method = payment_method
        self.amount = amount

    def get_flight_departure(self):
        return self.flight_departure

    def get_flight_destination(self):
        return self.flight_destination

    def get_flight_date(self):
        return self.flight_date

    def get_roomId(self):
        return self.roomId

    def get_check_in_date(self):
        return self.check_in_date

    def get_check_out_date(self):
        return self.check_out_date  

    def get_car_rental_location(self):
        return self.car_rental_location

    def get_car_rental_start_date(self):
        return self.car_rental_start_date

    def get_car_rental_end_date(self):
        return self.car_rental_end_date

    def get_payment_method(self):
        return self.payment_method

    def get_amount(self):
        return self.amount

    def set_flight_departure(self, flight_departure: str):
        self.flight_departure = flight_departure

    def set_flight_destination(self, flight_destination: str):
        self.flight_destination = flight_destination

    def set_flight_date(self, flight_date: str):
        self.flight_date = flight_date

    def set_roomId(self, roomId: str):
        self.roomId = roomId

    def set_check_in_date(self, check_in_date: str):
        self.check_in_date = check_in_date
        
    def set_check_out_date(self, check_out_date: str):
        self.check_out_date = check_out_date

    def set_car_rental_location(self, car_rental_location: str):
        self.car_rental_location = car_rental_location

    def set_car_rental_start_date(self, car_rental_start_date: str):
        self.car_rental_start_date = car_rental_start_date
    
    def set_car_rental_end_date(self, car_rental_end_date: str):
        self.car_rental_end_date = car_rental_end_date

    def set_payment_method(self, payment_method: str):
        self.payment_method = payment_method

    def set_amount(self, amount: float):
        self.amount = amount
