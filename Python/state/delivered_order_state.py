from order_state import OrderState

class DeliveredOrderState(OrderState):
    def __init__(self, order_management):
        self.order_management = order_management

    def process_order(self):
        print("Order cannot be processed because it's already delivered.")

    def ship_order(self):
        print("Order cannot be shipped because it's already delivered.")

    def deliver_order(self):
        print("Order is already delivered!")

    def cancel_order(self):
        print("Order cannot be cancelled because it's already delivered.")
