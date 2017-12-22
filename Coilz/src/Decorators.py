"Decorator learnings"

def double_out(old_function):
    "Decorator that doubles the result"
    def new_function(*args, **kwds):
        "Doubles the result of the original function"
        return 2*old_function(*args, **kwds)  # modify the return value
    return new_function

def double_in(old_function):
    "Decorator that doubles the provided argument"
    def new_function(arg):  # only works if the old function has one argument
        "Doubles the provided argument"
        return old_function(arg*2)  # modify the argument passed
    return new_function


def check(old_function):
    "Decorator that checks for positive numbers"
    def new_function(arg):
    "Checks for positive numbers"
        # This causes an error, which is better than it doing the wrong thing
        if arg < 0:
            raise ValueError("Negative value")
        old_function(arg)
    return new_function


def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return multiply_generator  # it returns the new generator


@multiply(3)  # Multiply is not a generator, but Multiply(3) is
def Num(num):
    return num


print(Num(4))

# --------------------------------


def type_check(correct_type):
    def type_checker(old_function):
        def new_function(arg):
            if not type(arg) is correct_type:
                print("Invalid type")
            return old_function(arg)
        return new_function
    return type_checker


@type_check(int)
def times2(num):
    return num*2


times2(2)
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


first_letter('Hello World')
first_letter(['Not', 'A', 'String'])
