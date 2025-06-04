from .PaymentMethod import PaymentMethod

class Visa(PaymentMethod):
    def __init__(self, card_holder: str, card_number: str, amount: float,
                 card_cvv: str, card_expiration_date: str):
        super().__init__(card_holder, card_number, amount, card_cvv, card_expiration_date)

    def authorize_payment(self):
        print(f"Authorizing payment of {self.amount} using {self.card_holder} with card number {self.card_number}")

    def start_money_transfer(self):
        print(f"Starting money transfer of {self.amount} using {self.card_holder} with card number {self.card_number}")

    def calculate_fee(self, amount: float):
        print(f"Calculating fee of {amount} using {self.card_holder} with card number {self.card_number}")
