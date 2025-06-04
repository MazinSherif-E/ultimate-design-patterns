from .PaymentMethod import PaymentMethod

class PaymentProcessor:
    def process_payment(self, paymentMethod: PaymentMethod, amount: float):
        print(f"Payment of {amount} processed with {paymentMethod.get_type()}")

