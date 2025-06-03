from abc import ABC, abstractmethod
from ScheduleManagementVisitor import ScheduleManagementVisitor

class ScheduleManagement(ABC):
    
    @abstractmethod
    def generateReport(self):
        pass
    
    @abstractmethod
    def calculateOverTime(self):
        pass
    
    @abstractmethod
    def accept(self, scheduleManagementVisitor: ScheduleManagementVisitor):
        pass