"""
Name: <Christopher Hamilton, II>
<sales_person>.py

Problem: This program creates a SalesPerson call

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    Creates a Sales_Person object
    """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        """
        Returns employee id
        """
        return self.employee_id

    def get_name(self):
        """
        Returns Name
        """
        return self.name

    def set_name(self, name):
        """
        Sets name
        """
        self.name = name

    def enter_sale(self, sale):
        """
        Adds sale(float) to sales list
        """
        self.sales.append(float(sale))

    def total_sales(self):
        """
        Returns sum of sales
        """
        return sum(self.sales)

    def get_sales(self):
        """
        Returns a list of sales
        """
        return self.sales

    def met_quota(self, quota):
        """
        Returns boolean comparing total sales to quota
        """
        return self.total_sales() >= quota

    def compare_to(self, other):
        """
        Returns an int value depending on the comparison
        """
        if self.total_sales() < other.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
