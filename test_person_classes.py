from person_classes import Customer, Employee

def test_customer():
    print("Testing Customer Class:")
    customer = Customer("12345", "Alice Smith", True)
    print(customer)
    customer.add_reward()
    customer.add_reward()
    print(f"Rewards: {customer.get_rewards()}")  # Should print 2
    print(f"Can redeem reward? {customer.redeem_rewards()}")  # Should print False
    print(f"Rewards after redeem attempt: {customer.get_rewards()}")  # Should print 2

def test_employee():
    print("\nTesting Employee Class:")
    employee = Employee("54321", "John Doe", 20.0, "09:00", "17:00")
    print(employee)
    print(f"Weekly Salary: {employee.get_weekly_salary()}")  # Should print 800.0
    print(f"Shift Time: {employee.get_shift_time_frame()}")  # Should print ('09:00', '17:00')

if __name__ == "__main__":
    test_customer()
    test_employee()
