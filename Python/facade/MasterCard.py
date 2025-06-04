from .PaymentMethod import PaymentMethod

class MasterCard(PaymentMethod):
    def get_type(self) -> str:
        return "master_card"


