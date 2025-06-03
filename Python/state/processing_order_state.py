from order_state import OrderState
from shipped_order_state import ShippedOrderState
from cancelled_order_state import CancelledOrderState

class ProcessingOrderState(OrderState):
    def __init__(self, order_management):
        self.order_management = order_management

    def process_order(self):
        print("The order is already being processed!")

    def ship_order(self):
        print("Shipping the order...")
        self.order_management.change_state(ShippedOrderState(self.order_management))

    def deliver_order(self):
        print("The order cannot be delivered at the current state.")

    def cancel_order(self):
        print("The order is being cancelled now...")
        self.order_management.change_state(CancelledOrderState(self.order_management))
