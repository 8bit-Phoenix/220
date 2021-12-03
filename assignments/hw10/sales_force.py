"""
Name: <Christopher Hamilton, II>
<sales_force>.py

Problem: This program creates a SalesForce class

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from sales_person import SalesPerson


class SalesForce:
    """
    Creates a SalesForce object
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        """
        Adds a list of SalesPerson objects from a file
        """
        with open(file_name, "r") as file:
            for line in file:
                e_id, name, sales = line.split(", ")
                s_person = SalesPerson(int(e_id), name)
                lst_sales = sales.strip()
                lst_sales = lst_sales.split()
                for i in lst_sales:
                    s_person.enter_sale(float(i))
                self.sales_people.append(s_person)
            file.close()

    def quota_report(self, quota):
        """
        Returns a list displaying if each SalesPerson made their quota
        """
        report_list = []
        for person in self.sales_people:
            person_list = [person.get_id(), person.get_name(), person.total_sales(),
                           person.met_quota(quota)]
            report_list.append(person_list)
        return report_list

    def top_seller(self):
        """
        Returns a list featuring the SalesPerson(s) with the most sales
        """
        top = [self.sales_people[0]]
        for i in self.sales_people:
            if top[0].compare_to(i) == -1:
                top = [i]
            elif not top[0].compare_to(i):
                top.append(i)
        return top

    def individual_sales(self, employee_id):
        """
        You enter the employee id, and it returns the corresponding SalesPerson object or none type
        """
        dictionary = {}
        for person in self.sales_people:
            dictionary[int(person.get_id())] = person
            if employee_id in dictionary:
                return dictionary.get(employee_id)
        return None
