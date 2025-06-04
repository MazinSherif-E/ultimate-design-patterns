from .PaymentMethod import PaymentMethod

class Paypal(PaymentMethod):
    def get_type(self) -> str:
        return "paypal"


