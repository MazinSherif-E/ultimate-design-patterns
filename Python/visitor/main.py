from DayShiftScheduleManagement import DayShiftScheduleManagement
from NightShiftScheduleManagement import NightShiftScheduleManagement
from RemoteWorkShiftScheduleManagement import RemoteWorkShiftScheduleManagement
from ManageLeaveRequestsVisitor import ManageLeaveRequestsVisitor

dayShiftscheduleManagement = DayShiftScheduleManagement()
dayShiftscheduleManagement.accept(ManageLeaveRequestsVisitor())

# nightShiftscheduleManagement = NightShiftScheduleManagement()
# nightShiftscheduleManagement.accept(ManageLeaveRequestsVisitor())

# remoteWorkShiftscheduleManagement = RemoteWorkShiftScheduleManagement()
# remoteWorkShiftscheduleManagement.accept(ManageLeaveRequestsVisitor())