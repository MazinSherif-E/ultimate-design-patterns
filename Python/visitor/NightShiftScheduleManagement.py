from ScheduleManagement import ScheduleManagement
from ScheduleManagementVisitor import ScheduleManagementVisitor

class NightShiftScheduleManagement(ScheduleManagement):
    def generateReport(self):
        print("Generate report for night shift schedule management")
    
    def calculateOverTime(self):
        print("Calculate over time for night shift schedule management")
        
    def accept(self, scheduleManagementVisitor: ScheduleManagementVisitor):
        scheduleManagementVisitor.visit(self)
