from abc import ABC, abstractmethod

class OrganisationUnit(ABC):
    @abstractmethod
    def calculate_total_salary(self) -> float:
        pass

