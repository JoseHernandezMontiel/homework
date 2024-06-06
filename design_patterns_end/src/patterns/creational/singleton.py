# Instance is one dependency for all project
# Focus points:
# - Watch for coupling by SINGLETON.
_instance = None

class Product:

    def __init__(self):
        self.weight = 0

    def do_operation(self):
        print(500)

    @staticmethod
    def get_instance():
        global _instance
        if _instance is None:
            _instance = Product()
        return _instance
