def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


transmit_to_space("Test message 1")


def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    return data_transmitter


message = transmit_to_space("Test message 2")
message()
message()


def multiplier_of(a):
    def multiply(b):
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
