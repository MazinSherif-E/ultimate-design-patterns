from ScheduleManagement import ScheduleManagement
from ScheduleManagementVisitor import ScheduleManagementVisitor

class RemoteWorkShiftScheduleManagement(ScheduleManagement):
    def generateReport(self):
        print("Generate report for remote work shift schedule management")
    
    def calculateOverTime(self):
        print("Calculate over time for remote work shift schedule management")
        
    def accept(self, scheduleManagementVisitor: ScheduleManagementVisitor):
        scheduleManagementVisitor.visit(self)
