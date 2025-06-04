from OrganisationUnit import OrganisationUnit

class Department(OrganisationUnit):
    def __init__(self):
        self.units = []

    def add_organisation_unit(self, unit: OrganisationUnit):
        self.units.append(unit)
    
    def remove_organisation_unit(self, unit: OrganisationUnit):
        self.units.remove(unit)
    
    def calculate_total_salary(self) -> float:
        return sum(unit.calculate_total_salary() for unit in self.units)
