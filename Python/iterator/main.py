from employee_hierarchy_collection import EmployeeHierarchyCollection

if __name__ == "__main__":
    employee_collection = EmployeeHierarchyCollection("123")

    print("\n--- Direct Report Iterator ---")
    direct_report_iterator = employee_collection.create_employee_direct_report_iterator()
    for employee in direct_report_iterator:
        print(employee)

    print("\n--- Co-Worker Iterator ---")
    coworker_iterator = employee_collection.create_employee_coworker_iterator()
    for employee in coworker_iterator:
        print(employee)

    print("\n--- Subordinate Iterator ---")
    subordinate_iterator = employee_collection.create_employee_subordinate_iterator()
    for employee in subordinate_iterator:
        print(employee)
