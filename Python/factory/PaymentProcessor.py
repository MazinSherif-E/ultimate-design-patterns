from .CardTypes import CardTypes
from .Visa import Visa
from .MasterCard import MasterCard
from .AmericanExpress import AmericanExpress
from .PaymentMethodFactory import PaymentMethodFactory

class PaymentProcessor:
    def process_payment(self, card_type: CardTypes, card_holder: str, card_number: str, amount: float,
                        card_cvv: str, card_expiration_date: str):
        
        payment_method = PaymentMethodFactory().create_payment_method(card_type, card_holder, card_number, amount, card_cvv, card_expiration_date)
        
        payment_method.authorize_payment()
        payment_method.start_money_transfer()
        payment_method.calculate_fee(amount)
        

