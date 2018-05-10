from decimal import *
import math as m
import string

c = DefaultContext
getcontext().prec = 8
setcontext(DefaultContext)
PHI = (Decimal(1) + Decimal(5).sqrt()) / Decimal(2)


class Base:

    def __init__(self, base, tolerance=0.000000001):
        if isinstance(base, int):
            if (base == 0 | base == 1 | base == -1):
                raise ValueError("Bad base")

            if base > 62:
                raise ValueError("Big base")

            if base > 10:
                self.digits = string.digits + string.ascii_letters[:(base-10)]

            else:
                self.digits = string.digits

            self.base = base

        else:
            self.base = Decimal(base)
            self.digits = "01"
        self.tolerance = tolerance


    def f(self, x):
        line = str(x)
        point = line.find(".")
        ret = Decimal(0)

        if point == -1:
            dim = Decimal(len(line) - 1)

            for n in line:
                if n not in self.digits:
                    raise ValueError("Bad input")
                ret += Decimal(self.digits.find(n)) * c.power(self.base, dim)
                dim -= 1

        else:
            dim = Decimal(point - 1)
            newline = line[:point] + line[point+1:]

            for n in newline:
                if n not in self.digits:
                    raise ValueError("Bad input")
                ret += Decimal(self.digits.find(n)) * c.power(self.base, dim)
                dim -= 1

        return float(ret)


    def t(self, x):
        num = Decimal(x)
        exp = lambda cur: cur.ln() / Decimal(self.base).ln()

        if isinstance(self.base, int):
            ret = ""
            while (num != 0):
                x = Decimal(str(
                        m.floor(exp(num))
                    ))
                n = Decimal(str(m.floor((
                                 num / (c.power(Decimal(self.base), x)
                    )))))
                num -= n * c.power(self.base, x)
                ret += f"{self.digits[int(n)]}"

        else:
            ret = 0
            while (num != 0):
                x = Decimal(str(m.floor(exp(num))))
                num -= c.power(self.base, x)
                ret += 10**x
                if -self.tolerance < num < self.tolerance:
                    break

        return f"{ret}"
