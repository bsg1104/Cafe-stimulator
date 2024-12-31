from person_classes import Customer, Employee
from rd_manager import Entry, QueueManager

def test_entry():
    print("Testing Entry Class:")
    customer = Customer("12345", "Alice Smith", True)
    entry = Entry(customer, "Latte", 4.5, "10:30")
    print(entry)

def test_queue_manager():
    print("\nTesting QueueManager Class:")
    manager = QueueManager()
    customer = Customer("12345", "Alice Smith", True)
    employee = Employee("54321", "John Doe", 15.0, "09:00", "17:00")
    entry = Entry(customer, "Latte", 4.5, "10:30")

    # Add Employee and Entry
    manager.enter_employee(employee)
    manager.add_entry(entry)
    print(f"Unresolved Entries: {len(manager)}")  # Should print 1

    # Process Entry
    next_entry = manager.get_next_entry()
    manager.add_resolved_entry(next_entry, employee)
    print(f"Resolved Entries: {len(manager.get_resolved_entries())}")  # Should print 1

if __name__ == "__main__":
    test_entry()
    test_queue_manager()
