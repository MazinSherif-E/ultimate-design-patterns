from .CardTypes import CardTypes
from .Visa import Visa
from .MasterCard import MasterCard
from .AmericanExpress import AmericanExpress

class PaymentMethodFactory:
    def create_payment_method(self, card_type: CardTypes, card_holder: str, card_number: str, amount: float,
                              card_cvv: str, card_expiration_date: str):
        if card_type == CardTypes.VISA:
            return Visa(card_holder, card_number, amount, card_cvv, card_expiration_date)
        elif card_type == CardTypes.MASTERCARD:
            return MasterCard(card_holder, card_number, amount, card_cvv, card_expiration_date)
        elif card_type == CardTypes.AMERICAN_EXPRESS:
            return AmericanExpress(card_holder, card_number, amount, card_cvv, card_expiration_date)
        else:
            raise ValueError(f"Invalid card type: {card_type}")
