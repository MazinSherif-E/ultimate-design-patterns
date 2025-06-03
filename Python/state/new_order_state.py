from order_state import OrderState
from processing_order_state import ProcessingOrderState
from cancelled_order_state import CancelledOrderState

class NewOrderState(OrderState):
    def __init__(self, order_management):
        self.order_management = order_management

    def process_order(self):
        print(f"Order: {self.order_management.order.name} is being processed now...")
        self.order_management.change_state(ProcessingOrderState(self.order_management))

    def ship_order(self):
        print(f"Cannot ship order: {self.order_management.order.name} at the current state.")

    def deliver_order(self):
        print(f"Cannot deliver order: {self.order_management.order.name} at the current state.")

    def cancel_order(self):
        print(f"Cancelling order: {self.order_management.order.name}")
        self.order_management.change_state(CancelledOrderState(self.order_management))
