from patterns.creational import singleton, builder, simple_factory
from patterns.structural import adapter, facade, decorator
from patterns.behavioral import chain_responsibility as cr
from patterns.behavioral import command, strategy
import time

def main():
    strategy_definition()

def singleton_definition():
    product1 = singleton.Product.get_instance()
    product2 = singleton.Product.get_instance()
    print(id(product1))
    print(id(product2))
    print(product1 == product2)
    print(product1.weight)

def builder_definition():
    product = (builder.ProductBuilder()
        .with_title("ProductA")
        .with_weight(100)
        .with_price(10.0)
        .with_ship_volume(5)
        .build())

    print(product.title, product.weight, product.price)

def simple_factory_definition():
    product_web = simple_factory.get_product("web")
    product_text = simple_factory.get_product("text")
    product_xml = simple_factory.get_product("xml")

    print(product_web)
    print(product_text)
    print(product_xml)


def adapter_definition():
    my_adapter = adapter.Adapter()
    other_adapter = singleton.Product.get_instance()
    operation_with_target(my_adapter)
    operation_with_target(other_adapter)

def operation_with_target(target):
    target.do_operation()


def facade_definition():
    op1, op2, op3 = facade.Facade().operation()
    print(op1)

def decorator_definition():
    message = decorator.Message("This is a message") # Type: Message
    textMessage = decorator.TextMessage(message) # Type: Text Message
    b64Message1 = decorator.Base64EncodedMessage(message) # Type: Base64EncodedMessage
    b64Message2 = decorator.Base64EncodedMessage(textMessage) # Type: Base64EncodedMessage

    # Liskov Substitution principle
    jsonMessage = decorator.JsonMessage(message) # Type: JsonMessage
    jsonMessage = decorator.JsonMessage(textMessage) # Type: JsonMessage
    jsonMessage = decorator.JsonMessage(b64Message1) # Type: JsonMessage
    jsonMessage = decorator.JsonMessage(b64Message2) # Type: JsonMessage

    print(message.get_content())
    print(textMessage.get_content())
    print(b64Message1.get_content())
    print(b64Message2.get_content())
    print(jsonMessage.get_content())

def chain_of_responsibility_definition():
    leave_request = cr.LeaveApplication(
        type="vacation",
        number_of_days = 10,
        status = "pending",
        processed_by = ""
    )

    manager = cr.Manager(None)
    lead = cr.Lead(manager) # xxx Head
    techLead = cr.TechLead(lead) # Head

    print(leave_request)

    techLead.process_leave_application(leave_request)

    print(leave_request)

def command_definition():
    service = command.EmailService()

    addEmailCmd1 = command.AddMemberCommand("mario@something.com", service)
    addEmailCmd2 = command.AddMemberCommand("javier@something.com", service)

    print(service.emails)
    # Crob job
    time.sleep(2)
    addEmailCmd2.execute()
    print(service.emails)
    time.sleep(1)
    addEmailCmd1.execute()
    print(service.emails)

def strategy_definition():
    array = [5, 90, 23, 67, 1, 8, 3]
    merge_strategy = strategy.MergeSort()
    quick_strategy = strategy.QuickSort()

    merge_strategy = strategy.ArraySorter(merge_strategy, array.copy())
    quick_strategy = strategy.ArraySorter(quick_strategy, array.copy())

    print(array)
    sorted_array_1 = merge_strategy.run_algorithm()
    print(sorted_array_1)
    sorted_array_2 = quick_strategy.run_algorithm()
    print(sorted_array_2)

if __name__ == '__main__':
    main()
