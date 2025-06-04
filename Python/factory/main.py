from .PaymentProcessor import PaymentProcessor
from .CardTypes import CardTypes
from .PaymentMethodFactory import PaymentMethodFactory

payment_processor = PaymentProcessor(PaymentMethodFactory())
payment_processor.process_payment(CardTypes.VISA, "John Doe", "1234567890123456", 100, "123", "12/2025")


