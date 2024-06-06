# Focus points
# - Command and Invoker are decoupled
# - How can we create a command for sending emails?
import abc

class Command(abc.ABC):

    def execute(self):
        raise Exception("I am an interface")


class AddMemberCommand(Command):

    def __init__(self, email, service):
        self.email = email
        self.service = service

    def execute(self):
        self.service.add_email(self.email)


class RemoveMemberCommand(Command):

    def __init__(self, email, service):
        self.email = email
        self.service = service

    def execute(self):
        self.service.remove_email(self.email)


class EmailService:

    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def remove_email(self, email):
        self.emails.append(email)