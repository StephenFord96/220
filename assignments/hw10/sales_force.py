"""
Name: Steve Ford
sales_force.py

Certificate of Authenticity:
I certify that this assignment is entirely my own work.

~~~~~~~~~~~~~~~~
~    Pseudo    ~
~     Code     ~
~~~~~~~~~~~~~~~~



"""
from sales_person import SalesPerson


class SalesForce:
    """This object holds all sales people objects"""

    # initializes the empty list of objects
    def __init__(self):
        self.sales_people = []

    # VOID; opens the file of data
    # ADDs all employees to sales_people list
    def add_data(self, file_name):
        # opens and reads file
        with open(file_name, "r") as infile:

            # loops through every line of the file
            for line in infile:

                # separates core, ID, Name, Sales
                person = line.split(", ")

                # instantiates a salesperson
                self.sales_people.append(SalesPerson(int(person[0]), person[1]))

                # splits up the string of sales
                sale_record = person[2].split()

                # loops through sales of the person and adds it to their record
                for sale in sale_record:
                    sale = float(sale)
                    self.sales_people[-1].enter_sale(sale)

    # returns a list of all employees with their ID, names, sales, and T/F of quota met
    def quota_report(self, quota):

        # initialize empty list of lists
        sheet = []

        # loop through every object in sale_people
        for person in self.sales_people:

            # initialize empty list for each person
            report = []

            # get and append information to individual report
            report.append(person.get_id())
            report.append(person.get_name())
            report.append(person.total_sales())
            report.append(person.met_quota(quota))

            # append finalized individual report/list to the list of ALL reports
            sheet.append(report)
        # return the list of lists
        return sheet

    # returns a list of the best sellers, list can have 1 element if no ties
    def top_seller(self):
        # sort all sales people in descending order based off their total sales
        self.sales_people.sort(key=lambda s: s.total_sales(), reverse=True)

        # if the 1st and 2nd position are not equal we no its a single winner
        if self.sales_people[0].total_sales() != self.sales_people[1].total_sales():
            return self.sales_people[:1]

        # otherwise see how many people are tied with the 1st index
        count = 1
        while self.sales_people[0].total_sales() == self.sales_people[count].total_sales():
            count += 1
        return self.sales_people[:count]

    # linear search for an object with the given id
    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None
