# Create a factory method for WebFactory
# Focus points:
# - The same module contains the factory code.
# - Add a new Entry to the factory.
from dataclasses import dataclass

@dataclass
class Web:
    url: str
    format: str

@dataclass
class Xml:
    url: str
    format: str

@dataclass
class Text:
    content: str
    format: str


def get_product(product_type: str):
    if product_type == "web":
        return Web("some url", "some format")
    elif product_type == "text":
        return Text("some text", "some format")
    elif product_type == "xml":
        return Xml("some url", "some format")
    else:
        raise Exception("Producto desconocido")