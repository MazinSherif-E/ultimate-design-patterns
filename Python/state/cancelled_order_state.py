from order_state import OrderState

class CancelledOrderState(OrderState):
    def __init__(self, order_management):
        self.order_management = order_management

    def process_order(self):
        print("Cannot process the order at the current state.")

    def ship_order(self):
        print("Cannot ship the order at the current state.")

    def deliver_order(self):
        print("Cannot deliver the order at the current state.")

    def cancel_order(self):
        print("Order is already cancelled!")
