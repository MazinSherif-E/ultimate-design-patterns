from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, card_holder: str, card_number: str, amount: float,
                 card_cvv: str, card_expiration_date: str):
        self.card_holder = card_holder
        self.card_number = card_number
        self.amount = amount
        self.card_cvv = card_cvv
        self.card_expiration_date = card_expiration_date
        
    def set_card_holder(self, card_holder: str):
        self.card_holder = card_holder

    def set_card_number(self, card_number: str):
        self.card_number = card_number

    def set_amount(self, amount: float):
        self.amount = amount

    def set_card_cvv(self, card_cvv: str):
        self.card_cvv = card_cvv

    def set_card_expiration_date(self, card_expiration_date: str):
        self.card_expiration_date = card_expiration_date
    
    @abstractmethod
    def authorize_payment(self):
        pass

    @abstractmethod
    def start_money_transfer(self):
        pass

    @abstractmethod
    def calculate_fee(self, amount: float):
        pass
    
    
