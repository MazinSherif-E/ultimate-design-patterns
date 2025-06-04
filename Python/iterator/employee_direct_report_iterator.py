from employee_hierarchy_iterator import EmployeeHierarchyIterator

class EmployeeDirectReportIterator(EmployeeHierarchyIterator):
    def __init__(self, employee_list):
        self.employees = employee_list
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.employees):
            raise StopIteration
        print("Iterating through direct reports...")
        employee = self.employees[self.position]
        self.position += 1
        return employee
