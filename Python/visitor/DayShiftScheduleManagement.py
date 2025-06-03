from ScheduleManagement import ScheduleManagement
from ScheduleManagementVisitor import ScheduleManagementVisitor

class DayShiftScheduleManagement(ScheduleManagement):
    def generateReport(self):
        print("Generate report for day shift schedule management")
    
    def calculateOverTime(self):
        print("Calculate over time for day shift schedule management")
        
    def accept(self, scheduleManagementVisitor: ScheduleManagementVisitor):
        scheduleManagementVisitor.visit(self)
