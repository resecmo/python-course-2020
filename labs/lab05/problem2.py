from math import gcd


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError(f"Denominator is zero")
        elif denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def reduce(self):
        factor = gcd(self.__numerator, self.__denominator)
        self.__numerator //= factor
        self.__denominator //= factor

    def __float__(self):
        return self.__numerator / self.__denominator

    def __neg__(self):
        return Rational(-self.__numerator, self.__denominator)

    def __add__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                                    self.__denominator * other.__denominator)
            return_value.reduce()
        elif isinstance(other, int):
            return_value = Rational(self.__numerator + other * self.__denominator, self.__denominator)
        else:
            raise TypeError(f"Cannot add {type(other)} to Rational")
        return return_value

    def __radd__(self, other):
        if isinstance(other, int):
            return self + other
        else:
            raise TypeError(f"Cannot add {type(other)} to Rational")

    def __sub__(self, other):  # possibly bad for call stack?
        if isinstance(other, (Rational, int)):
            return_value = self + (-other)
        else:
            raise TypeError(f"Cannot subtract {type(other)} from Rational")
        return return_value

    def __rsub__(self, other):
        if isinstance(other, int):
            return -(self - other)
        else:
            raise TypeError(f"Cannot subtract {type(other)} from Rational")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)
        elif isinstance(other, int):
            return_value = Rational(self.__numerator * other, self.__denominator)
        else:
            raise TypeError(f"Cannot multiply {type(other)} by Rational")
        return_value.reduce()
        return return_value

    def __rmul__(self, other):
        if isinstance(other, int):
            return self * other
        else:
            raise TypeError(f"Cannot multiply {type(other)} by Rational")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)
        elif isinstance(other, int):
            return_value = Rational(self.__numerator, self.__denominator * other)
        else:
            raise TypeError(f"Cannot multiply Rational by {type(other)}")
        return_value.reduce()
        return return_value

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(self.__denominator * other, self.__numerator)
        else:
            raise TypeError(f"Cannot divide {type(other)} by Rational")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.__numerator == other.__numerator and self.__denominator == other.__denominator
        elif isinstance(other, int):
            return self.__numerator == other and self.__denominator == 1
        else:
            raise TypeError(f"Cannot compare {type(other)} and Rational")

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    @classmethod
    def from_string(cls, string):
        numbers_list = string.split('/')
        if not len(numbers_list) == 2:
            raise ValueError(f"{string} cannot be read as rational")
        else:
            try:
                num, denom = [int(x) for x in numbers_list]
            except ValueError as e:
                raise ValueError(f"Numerator or denominator is not integer in \"{string}\"")
            if denom <= 0:
                raise ValueError(f"Denominator is nonpositive in \"{string}\"")
            return Rational(num, denom)


def test_operations():
    assert Rational(3, 5) + Rational(3, 5) == Rational(6, 5)
    assert Rational(3, 5) + Rational(2, 5) == 1
    assert Rational(3, 5) + 2 == Rational(13, 5)
    assert 7 + Rational(3, 5) == Rational(38, 5)

    assert Rational(4, 7) - 2 == Rational(-10, 7)
    assert 7 - Rational(40, 7) == Rational(9, 7)

    assert Rational(7, 2) * Rational(3, 1) == Rational(21, 2)
    assert Rational(7, 2) * Rational(2, 1) == 7
    assert Rational(7, 2) * 2 == 7
    assert 5 * Rational(3, 25) == Rational(3, 5)
    assert 5 * Rational(3, 30) == Rational(1, 2)

    assert Rational(5, 7) / Rational(5, 7) == 1
    assert 6 / Rational(12, 5) == Rational(5, 2)

    assert Rational(5, 6) == Rational(5, 6)
    assert Rational(13, 6) == Rational(26, 12)
    assert Rational(36, 6) == 6
    assert Rational(36, 6) != 7
    assert 8 != Rational(4, 6)


def test_cast_to_float():
    assert float(Rational(5, 7)) == 5/7
    assert float(Rational(0, 1)) == 0
    assert float(Rational(42, 10**20)) == 42 / 10**20
    assert float(Rational(12**48, 48)) == 12**48 / 48


def test_parse_from_string():
    assert Rational.from_string("3/3") == 1
    assert Rational.from_string("0/1") == 0
    assert Rational.from_string("-7/6") == Rational(-7, 6)
    assert Rational.from_string("-3512351325/513451345") == Rational(-3512351325, 513451345)

    try:
        Rational.from_string("0/0")
    except ValueError as e:
        assert str(e) == "Denominator is nonpositive in \"0/0\""

    try:
        Rational.from_string("7/-6")
    except ValueError as e:
        assert str(e) == "Denominator is nonpositive in \"7/-6\""

    try:
        Rational.from_string("4.0/1")
    except ValueError as e:
        assert str(e) == "Numerator or denominator is not integer in \"4.0/1\""


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()
