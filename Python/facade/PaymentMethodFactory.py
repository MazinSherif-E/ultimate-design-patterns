from .PaymentMethodOptions import PaymentMethodOptions
from .VisaCard import VisaCard
from .MasterCard import MasterCard
from .PayPal import Paypal

class PaymentMethodFactory:
    def create_payment_method(self, payment_method: str) -> PaymentMethodOptions: 
        if payment_method == PaymentMethodOptions.VISA:
            return VisaCard()
        elif payment_method == PaymentMethodOptions.MASTER_CARD:
            return MasterCard()
        elif payment_method == PaymentMethodOptions.PAYPAL:
            return Paypal()
        else:
            raise ValueError(f"Invalid payment method: {payment_method}")