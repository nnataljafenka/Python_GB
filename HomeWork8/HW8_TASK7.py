class Complex():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __add__(self, other):
        a_res = self.a + other.a
        b_res = self.b + other.b
        return Complex(a_res, b_res)

    def __mul__(self, other):
        a_res = (self.a * other.a) - (self.b * other.b)
        b_res = (self.a * other.b) + (self.b * other.a)
        return Complex(a_res, b_res)

    def __str__(self):
        return f"{self.a} + {self.b}i" if int(self.a) != 0 and int(self.b) != 0 else f"{self.b}i" if int(self.b) != 0 else f"{self.a}"


z_1 = Complex(1, 2)
z_2 = Complex(3, 4)
z_3 = Complex(0, 1)
print(z_1 + z_2)
print()
print(z_1 * z_2)
print()
print(z_3 * z_3)
