class Complex:
    def __init__(self, re=0, im=0):
        """
        re: int, float
        im: int, float
        """

        if not isinstance(re, (float, int)) or not isinstance (im, (float, int)):
            raise TypeError("Both arguments must be real numbers")
        self.re = re
        self.im = im

    def __str__(self) -> str:
        if self.im < 0:
            return f"{self.re}{self.im}i"
        else:
            return f"{self.re}+{self.im}i"

    def __add__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        if isinstance(other, Complex):
            return Complex (self.re + other.re, self.im + other.im)
        elif isinstance(other, (float, int)):
            return Complex (self.re + other, self.im)
        else:
            raise TypeError("Argument must be a real or a complex number")


    def __sub__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (float, int)):
            return Complex(self.re - other, self.im)
        else:
            raise TypeError("Argument must be a real or a complex number")

    def __mul__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        elif isinstance(other, (float, int)):
            return Complex(self.re * other, self.im * other)
        else:
            raise TypeError("Argument must be a real or a complex number")

    def __truediv__(self, other) -> "Complex":
        """
        other: int, float, Complex
        """
        if isinstance(other, Complex):
            denom = other.re ** 2 + other.im ** 2
            return Complex((self.re * other.re + self.im * other.im) / denom,
                           (self.im * other.re - self.re * other.im) / denom)
        elif isinstance(other, (int, float)):
            return Complex(self.re / other, self.im / other)
        else:
            raise TypeError("Argument must be a number or a Complex object")

    # Part 4
    def __eq__(self, other) -> bool:
        """
        other: Complex
        """
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        else:
            return False
    def __abs__(self) -> float:
        return (self.re ** 2 + self.im ** 2) ** 0.5