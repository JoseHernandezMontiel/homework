# Focus points:
# - show duck typing
# - How can we adapt to a different Target?
import abc
import requests

class Target(abc.ABC):

    def do_operation(self):
        raise Exception("I am a base class")


class Adapter:

    def do_operation(self):
        x = requests.get("https://google.com")
        print(x.status_code)