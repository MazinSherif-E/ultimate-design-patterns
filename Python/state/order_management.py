from new_order_state import NewOrderState

class OrderManagement:
    def __init__(self, order):
        self.order = order
        self.order_state = NewOrderState(self)  # Initial state

    def change_state(self, new_state):
        self.order_state = new_state

    def process_order(self):
        self.order_state.process_order()

    def ship_order(self):
        self.order_state.ship_order()

    def deliver_order(self):
        self.order_state.deliver_order()

    def cancel_order(self):
        self.order_state.cancel_order()
