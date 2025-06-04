from employee import Employee
from employee_direct_report_iterator import EmployeeDirectReportIterator
from employee_coworker_iterator import EmployeeCoWorkerIterator
from employee_subordinate_iterator import EmployeeSubOrdinateIterator
from iterable_collection import IterableCollection

class EmployeeHierarchyCollection(IterableCollection):
    def __init__(self, employee_id: str):
        self.employee_id = employee_id
        self.employees = [
            Employee("123", "Mahmoud"),
            Employee("345", "Ahmed"),
            Employee("678", "Sarah")
        ]

    def get_employees(self):
        return self.employees

    def create_employee_direct_report_iterator(self):
        return EmployeeDirectReportIterator(self.employees)

    def create_employee_coworker_iterator(self):
        return EmployeeCoWorkerIterator(self.employees)

    def create_employee_subordinate_iterator(self):
        return EmployeeSubOrdinateIterator(self.employees)
