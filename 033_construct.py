class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im


a = Complex(1, 2)
b = Complex(3)
c = Complex()
print(a.re, a.im)
print(b.re, b.im)
print(c.re, c.im)


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep


a = Complex(1, 2)
print(a)
b = Complex(3, -4.5)
print(b)


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep

    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)


a = Complex(1, 2)
b = Complex(3, -4.5)
print(a + b)


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        strRep = str(self.re)
        if self.im >= 0:
            strRep += '+'
        strRep += str(self.im) + 'i'
        return strRep

    def __add__(self, other):
        newRe = self.re + other.re
        newIm = self.im + other.im
        return Complex(newRe, newIm)

    def __mul__(self, other):
        if isinstance(other, Complex):
            newRe = self.re * other.re - self.im * other.im
            newIm = self.re * other.im + self.im * other.re
        elif isinstance(other, int) or isinstance(other, float):
            newRe = self.re * other
            newIm = self.im * other
        return Complex(newRe, newIm)

    __rmul__ = __mul__


a = Complex(1, 2)
b = Complex(3, -4.5)
print(a * b)
print(a * 2)