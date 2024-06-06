# Hide dependencies in single operation
# Focus Points:
# - One method interacts with others
# - prevent abusing
import requests

class Facade:

    def operation(self):
        op1 = external_operation_1()
        op2 = external_operation_2()
        op3 = external_operation_3()

        return op1, op2, op3


def external_operation_1():
    pokemon_data = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    return pokemon_data.json()


def external_operation_2():
    pokemon_data = requests.get("https://pokeapi.co/api/v2/type/3")
    return pokemon_data.json()

def external_operation_3():
    pokemon_data = requests.get("https://pokeapi.co/api/v2/ability/battle-armor")
    return pokemon_data.json()
