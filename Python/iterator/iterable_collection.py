from abc import ABC, abstractmethod

class IterableCollection(ABC):
    @abstractmethod
    def create_employee_direct_report_iterator(self):
        pass

    @abstractmethod
    def create_employee_coworker_iterator(self):
        pass

    @abstractmethod
    def create_employee_subordinate_iterator(self):
        pass
