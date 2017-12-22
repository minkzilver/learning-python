"Closure learnings"

def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


transmit_to_space("Test message 1")


def return_from_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    return data_transmitter


transmit = return_from_space("Test message 2")
transmit()
transmit()


def multiplier_of(a):
    "This is the enclosing function"
    def multiply(b):
        "The nested function"
        return a*b

    return multiply


multiplywith5 = multiplier_of(5)
product = multiplywith5(9)
print(product)

multiplywith4 = multiplier_of(4)
product = multiplywith4(9)
print(product)

product = multiplywith5(2)
print(product)
