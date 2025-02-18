# Task 4 Employeer salary by hours.

class EmployeeSalary:
    """Something."""

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        return self.hours * self.hourly_payment
    

# test code:
# Sam = EmployeeSalary.get_hours("Sam", 5, "Q@Q")
# print(Sam.hours)
# Paul = EmployeeSalary.get_email("Paul", 6, 5)
# print(Paul.email)
# EmployeeSalary.set_hourly_payment(200)
# print(EmployeeSalary.hourly_payment)
# print(Sam.salary())