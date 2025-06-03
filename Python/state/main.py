from order import Order
from order_management import OrderManagement

# Create an order
order = Order("Laptop", 1000)
order_management = OrderManagement(order)

# Simulating the order process
order_management.process_order()  # Moves to ProcessingOrderState
order_management.ship_order()     # Moves to ShippedOrderState
order_management.deliver_order()  # Moves to DeliveredOrderState
order_management.cancel_order()   # Should not be possible
