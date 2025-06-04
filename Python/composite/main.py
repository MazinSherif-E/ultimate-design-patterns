from Employee import Employee
from Department import Department

hrDepartment = Department()
hrDepartment.add_organisation_unit(Employee("John", 1000))
hrDepartment.add_organisation_unit(Employee("Jane", 1500))

itDepartment = Department()
itDepartment.add_organisation_unit(Employee("Alice", 2000))
itDepartment.add_organisation_unit(Employee("Bob", 2500))

hrDepartment.add_organisation_unit(itDepartment)

print(hrDepartment.calculate_total_salary())