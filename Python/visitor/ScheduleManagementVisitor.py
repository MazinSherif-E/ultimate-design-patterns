from abc import ABC, abstractmethod

class ScheduleManagementVisitor(ABC):
    @abstractmethod
    def visit(self, scheduleManagement):
        pass
    
    