"""
Name: Steve Ford
sales_person.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """This holds all the information of a sales person"""
    # constructor with ID, name, and list of floats as sales
    # ensures proper data types are used to instantiate object
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = str(name)
        self.sales = []

    # returns the employee's ID
    def get_id(self):
        return self.employee_id

    # returns the employee's name
    def get_name(self):
        return self.name

    # VOID; changes the employee's name
    def set_name(self, name):
        self.name = name

    # VOID; adds a sale/float to list of sales
    def enter_sale(self, sale):
        self.sales.append(sale)

    # returns the sum of all sales
    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc += sale
        return acc

    # returns the list of all sales
    def get_sales(self):
        return self.sales

    # returns T/F if employee reached the quota
    def met_quota(self, quota):
        if quota <= self.total_sales():
            return True
        return False

    # returns -1/0/+1 after comparing sales with another employee
    def compare_to(self, other):
        my_sales = self.total_sales()
        other_sales = other.total_sales()
        if my_sales < other_sales:
            return -1
        if my_sales > other_sales:
            return 1
        return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
