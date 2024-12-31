from rd_client import prompt_add_employee, take_next_order, log_resolved_orders, log_unresolved_orders
from rd_manager import QueueManager, Entry
from person_classes import Customer

def test_client():
    print("Testing rd_client:")
    manager = QueueManager()

    # Add Employee
    print("\nAdding Employee:")
    prompt_add_employee(manager)

    # Add Customer Entry
    customer = Customer("12345", "Alice Smith", True)
    entry = Entry(customer, "Latte", 4.5, "10:30")
    manager.add_entry(entry)

    # Process Order
    print("\nProcessing Order:")
    take_next_order(manager)

    # Log Results
    print("\nLogging Results:")
    log_resolved_orders(manager, "resolved_orders.csv")
    log_unresolved_orders(manager, "unresolved_orders.csv")
    print("Logs created: resolved_orders.csv, unresolved_orders.csv")

if __name__ == "__main__":
    test_client()
