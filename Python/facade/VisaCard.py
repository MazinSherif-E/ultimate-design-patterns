from .PaymentMethod import PaymentMethod

class VisaCard(PaymentMethod):
    def get_type(self) -> str:
        return "visa"


