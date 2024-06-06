import base64
# Focus Points
# - Duck Typing
# - Composing Types
# How to add another decorator?
class Message:
    def __init__(self, msg):
        self.msg = msg

    def get_content(self):
        return self.msg

class TextMessage:

    def __init__(self, message):
        self.message = message

    def get_content(self):
        return f"\t {self.message.get_content()} \n"

class Base64EncodedMessage:
    def __init__(self, message):
        self.message = message

    def get_content(self):
        bytes_str = str.encode(self.message.get_content())
        base64_bytes = base64.b64encode(bytes_str)
        return base64_bytes.decode("ascii")


class JsonMessage:
    def __init__(self, message):
        self.message = message

    def get_content(self):
        return '{ "msg": "' + self.message.get_content() + '"}'
