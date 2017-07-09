class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, c):
        return Complex(self.r + c.r, self.i + c.i)
