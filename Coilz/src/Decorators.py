def Double_Out(old_function):
    def new_function(*args, **kwds):
        return 2*old_function(*args, **kwds)  # modify the return value
    return new_function


def Double_In(old_function):
    def new_function(arg):  # only works if the old function has one argument
        return old_function(arg*2)  # modify the argument passed
    return new_function


def Check(old_function):
    def new_function(arg):
        # This causes an error, which is better than it doing the wrong thing
        if arg < 0:
            raise ValueError("Negative value")
        old_function(arg)
    return new_function


def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwds):
            return multiplier*old_function(*args, **kwds)
        return new_function
    return Multiply_Generator  # it returns the new generator


@Multiply(3)  # Multiply is not a generator, but Multiply(3) is
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
