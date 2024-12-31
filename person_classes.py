class Customer:
    POINTS_NEEDED_FOR_REWARD = 10

    def __init__(self, cust_id, name, is_student):
        """
        Initializes a Customer instance.
        :param cust_id: Unique customer ID (str)
        :param name: Full name of the customer (str)
        :param is_student: Boolean indicating if the customer is a student
        """
        self.cust_id = cust_id
        self.name = name
        self.is_student = is_student
        self.rewards = 0

    def get_cust_id(self):
        return self.cust_id

    def get_name(self):
        return self.name

    def is_caltech_student(self):
        return self.is_student

    def get_rewards(self):
        return self.rewards

    def add_reward(self):
        self.rewards += 1

    def redeem_rewards(self):
        """
        Redeems reward points if the customer has enough.
        :return: True if rewards were redeemed, False otherwise.
        """
        if self.rewards >= Customer.POINTS_NEEDED_FOR_REWARD:
            self.rewards -= Customer.POINTS_NEEDED_FOR_REWARD
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of the Customer object.
        """
        return (f"Name: {self.name}\n"
                f"ID: {self.cust_id}\n"
                f"Rewards: {self.rewards}\n"
                f"Is Student?: {self.is_student}")


class Employee:
    def __init__(self, emp_id, name, hourly_wage, start_time, end_time):
        """
        Initializes an Employee instance.
        :param emp_id: Unique employee ID (str)
        :param name: Full name of the employee (str)
        :param hourly_wage: Hourly wage of the employee (float)
        :param start_time: Shift start time (str, HH:MM format)
        :param end_time: Shift end time (str, HH:MM format)
        """
        self.emp_id = emp_id
        self.name = name
        self.hourly_wage = hourly_wage
        self.start_time = start_time
        self.end_time = end_time

    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_weekly_salary(self):
        """
        Calculates weekly salary based on a 5-day, 8-hour workweek.
        :return: Weekly salary (float)
        """
        return self.hourly_wage * 8 * 5

    def get_shift_time_frame(self):
        """
        Returns the start and end times of the employee's shift.
        :return: Tuple containing (start_time, end_time)
        """
        return self.start_time, self.end_time

    def __str__(self):
        """
        Returns a string representation of the Employee object.
        """
        return (f"Name: {self.name}\n"
                f"ID: {self.emp_id}\n"
                f"Weekly Salary: ${self.get_weekly_salary():.2f}\n"
                f"Shift Time: {self.start_time}-{self.end_time}")
