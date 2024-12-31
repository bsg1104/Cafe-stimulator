class Entry:
    def __init__(self, customer, order, price, timestamp):
        """
        Initializes an Entry instance.
        :param customer: Customer object
        :param order: String describing the item ordered
        :param price: Float price of the order
        :param timestamp: String timestamp of the order (HH:MM)
        """
        self.customer = customer
        self.order = order
        self.price = price
        self.timestamp = timestamp
        self.response_employee = None
        self.wait_time = -1  # Default unresolved

    def get_order(self):
        return self.order

    def get_customer(self):
        return self.customer

    def get_response_employee(self):
        return self.response_employee

    def get_price(self):
        return self.price

    def get_wait_time(self):
        return self.wait_time

    def __str__(self):
        customer_str = str(self.customer)
        return f"{customer_str}\nPrice of {self.order}: {self.price}"


class QueueManager:
    def __init__(self):
        """Initializes the QueueManager with empty lists and a dictionary."""
        self.unresolved_entries = []
        self.resolved_entries = []
        self.employees = {}

    def __len__(self):
        return len(self.unresolved_entries)

    def enter_employee(self, employee):
        emp_id = employee.get_emp_id()
        if emp_id in self.employees:
            print("This Employee is already in the QueueManager.")
        else:
            self.employees[emp_id] = employee

    def get_employee(self, emp_id):
        return self.employees.get(emp_id, None)

    def add_entry(self, entry):
        if entry not in self.unresolved_entries:
            self.unresolved_entries.append(entry)
        else:
            print("Duplicate entry. Order already exists in the queue.")

    def get_next_entry(self):
        if not self.unresolved_entries:
            return None
        return self.unresolved_entries.pop(0)

    def add_resolved_entry(self, entry, employee):
        entry.response_employee = employee
        # Optionally calculate wait time here if needed
        self.resolved_entries.append(entry)

    def get_resolved_entries(self):
        return self.resolved_entries

    def get_unresolved_entries(self):
        return self.unresolved_entries

    def remove_employee(self, emp_id):
        """Removes an employee from the queue manager."""
        if emp_id in self.employees:
            del self.employees[emp_id]
        else:
            print("Employee not found.")
