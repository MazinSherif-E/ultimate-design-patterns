class Employee:
    def __init__(self, emp_id: str, name: str):
        self.id = emp_id
        self.name = name

    def __str__(self):
        return f"Employee[ID={self.id}, Name={self.name}]"
