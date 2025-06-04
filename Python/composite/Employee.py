from OrganisationUnit import OrganisationUnit

class Employee(OrganisationUnit):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def calculate_total_salary(self) -> float:
        return self.salary

