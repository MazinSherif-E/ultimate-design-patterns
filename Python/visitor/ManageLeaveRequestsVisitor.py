from ScheduleManagementVisitor import ScheduleManagementVisitor
from DayShiftScheduleManagement import DayShiftScheduleManagement
from NightShiftScheduleManagement import NightShiftScheduleManagement
from RemoteWorkShiftScheduleManagement import RemoteWorkShiftScheduleManagement

class ManageLeaveRequestsVisitor(ScheduleManagementVisitor):
    def visit(self, scheduleManagement):
        if isinstance(scheduleManagement, DayShiftScheduleManagement):
            print("Manage leave requests for day shift schedule management")
        elif isinstance(scheduleManagement, NightShiftScheduleManagement):
            print("Manage leave requests for night shift schedule management")
        elif isinstance(scheduleManagement, RemoteWorkShiftScheduleManagement):
            print("Manage leave requests for remote work shift schedule management")