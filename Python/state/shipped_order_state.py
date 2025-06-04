from order_state import OrderState
from delivered_order_state import DeliveredOrderState

class ShippedOrderState(OrderState):
    def __init__(self, order_management):
        self.order_management = order_management

    def process_order(self):
        print("Cannot process the order at the current state.")

    def ship_order(self):
        print("The order is currently being shipped!")

    def deliver_order(self):
        print("Delivering order now...")
        self.order_management.change_state(DeliveredOrderState(self.order_management))

    def cancel_order(self):
        print("Cannot cancel the order at the current state.")
