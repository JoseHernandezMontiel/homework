# Focus Points
# - Main method needs to construct the chain
# - Everyone has a chance to process the request
from dataclasses import dataclass
import abc

@dataclass
class LeaveApplication:
    type: str
    number_of_days: int
    status: str
    processed_by: str


class LeaveApprover(abc.ABC):

    def process_leave_application(self, leave_application):
        raise Exception("I am an interface")


class Employee:

    def __init__(self, role, successor):
        self.role = role
        self.successor = successor

    def process_leave_application(self, leave_application):
        if not self.process_request(leave_application) and self.successor is not None:
            self.successor.process_leave_application(leave_application)

    def process_request(self, leave_application) -> bool:
        pass

class TechLead(Employee):

    def __init__(self, successor):
        super().__init__("TechLead", successor)

    def process_request(self, leave_application) -> bool:
        if leave_application.number_of_days == 1:
            leave_application.status = "resolved"
            leave_application.processed_by = self.role
            return True
        else:
            return False

class Lead(Employee):

    def __init__(self, successor):
        super().__init__("Lead", successor)

    def process_request(self, leave_application) -> bool:
        if leave_application.number_of_days < 5:
            leave_application.status = "resolved"
            leave_application.processed_by = self.role
            return True
        else:
            return False

class Manager(Employee):

    def __init__(self, successor):
        super().__init__("Manager", successor)

    def process_request(self, leave_application) -> bool:
        if leave_application.number_of_days > 5:
            leave_application.status = "resolved"
            leave_application.processed_by = self.role
            return True
        else:
            return False