import csv


def prompt_add_employee(queue_manager):
    name = input("Enter the Employee's name: ")
    emp_id = input("Enter the Employee's ID: ")
    hourly_wage = float(input("Enter the Employee's Hourly Wage: "))
    start_time = input("Enter start time for your shift in HH:MM format (hours 0-23): ")
    end_time = input("Enter end time for your shift in HH:MM format (hours 0-23): ")
    add_employee(queue_manager, emp_id, name, hourly_wage, start_time, end_time)


def add_employee(queue_manager, emp_id, name, hourly_wage, start_time, end_time):
    from person_classes import Employee
    employee = Employee(emp_id, name, hourly_wage, start_time, end_time)
    queue_manager.enter_employee(employee)


def take_next_order(queue_manager):
    if not queue_manager.unresolved_entries:
        print("No orders currently waiting to be taken.")
        return

    emp_id = input("Enter the answering Employee's ID: ")
    employee = queue_manager.get_employee(emp_id)
    if not employee:
        print("Employee not found.")
        return

    next_entry = queue_manager.get_next_entry()
    if not next_entry:
        print("No orders currently waiting to be taken.")
        return

    print(next_entry)
    resolve = input('Enter "y" if the order has been taken. ')
    if resolve.lower() == 'y':
        queue_manager.add_resolved_entry(next_entry, employee)
    else:
        queue_manager.add_entry(next_entry)


def log_resolved_orders(queue_manager, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['price', 'order', 'wait_time', 'response_employee', 'employee_timeframe'])
        writer.writeheader()
        for entry in queue_manager.get_resolved_entries():
            writer.writerow({
                'price': entry.get_price(),
                'order': entry.get_order(),
                'wait_time': entry.get_wait_time(),
                'response_employee': entry.response_employee.get_name(),
                'employee_timeframe': entry.response_employee.get_shift_time_frame()
            })


def log_unresolved_orders(queue_manager, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['customer_id', 'customer_name', 'price', 'order'])
        writer.writeheader()
        for entry in queue_manager.get_unresolved_entries():
            writer.writerow({
                'customer_id': entry.get_customer().get_cust_id(),
                'customer_name': entry.get_customer().get_name(),
                'price': entry.get_price(),
                'order': entry.get_order()
            })
