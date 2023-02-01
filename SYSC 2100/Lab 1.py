# Tauheed Alamgir 101194927

# SYSC 2100 Winter 2022, Lab 1
# Last edited: Jan. 14, 2022

def gcd(m: int, n: int) -> int:
    """Return the greatest common divisor of m and n.

    Precondition: m > 0, n > 0.

    >>> gcd(4, 1)
    1
    >>> gcd(30, 5)
    5
    >>> gcd(9, 17)
    1
    """
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, n: int, d: int) -> None:
        """Initialize self with numerator n and denominator d.

        Raise a ValueError exception if d is 0.

        When __init__ returns, this fraction will be in reduced form.
        This means that:
        (1) if the numerator is equal to 0, the denominator is always 1.
        (2) if the numerator is not equal to 0, the denominator is always
        positive. This means that negative fractions always have a negative
        numerator and a positive denominator.
        (3) the numerator and denominator have no common divisors other than 1.

        >>> Fraction(3, 4)
        Fraction(3, 4)
        >>> Fraction(6, 8)
        Fraction(3, 4)
        >>> Fraction(-3, 4)
        Fraction(-3, 4)
        >>> Fraction(3, -4)
        Fraction(-3, 4)
        >>> Fraction(-3, -4)
        Fraction(3, 4)
        >>> Fraction(0, 5)
        Fraction(0, 1)
        """

        # This method must be modified to match the specification
        # in the docstring.

        if __name__ == '__main__':
            self._num = n
            self._den = d
            t = gcd(self._num, self._den)
            self._num = self._num // t
            self._den = self._den // t

    def __str__(self) -> str:
        """Return a string representation of self in the format: 'n/d'.

        >>> f = Fraction(3, 4)
        >>> str(f)
        '3/4'
        >>> f = Fraction(6, -8)
        >>> str(f)
        '-3/4'
        """
        if __name__ == '__main__':
            return (str(self._num) + '/' + str(self._den))

    def __repr__(self) -> str:
        """Return a string representation of self in the format:
        'Fraction(n, d)'.

        >>> f = Fraction(3, 4)
        >>> repr(f)
        'Fraction(3, 4)'
        >>> f = Fraction(6, -8)
        >>> repr(f)
        'Fraction(-3, 4)'
        """
        return "Fraction({0}, {1})".format(self._num, self._den)

    def numerator(self) -> int:
        """Return the numerator of self.

        >>> f = Fraction(3, 4)
        >>> f.numerator()
        3
        """
        if __name__ == '__main__':
            return self._num

    def denominator(self) -> int:
        """Return the denominator of self.

        >>> f = Fraction(3, 4)
        >>> f.denominator()
        4
        """
        if __name__ == '__main__':
            return self._den

    def __add__(self, other_fraction: 'Fraction') -> 'Fraction':
        """Return the sum of self and other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 + f2
        Fraction(7, 8)
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> f1 + f2
        Fraction(3, 4)
        """
        if __name__ == '__main__':
            nume = (self._num * other_fraction._den) + (self._den * other_fraction._num)
            deno = self._den * other_fraction._den
        return Fraction(nume, deno)

    def __sub__(self, other_fraction: 'Fraction') -> 'Fraction':
        """Return the difference of self and other_fraction; that is,
        the Fraction that is obtained by subtracting other_fraction from self.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 - f2
        Fraction(5, 8)
        >>> f1 = Fraction(1, 4)
        >>> f2 = Fraction(1, 2)
        >>> f1 - f2
        Fraction(-1, 4)
        """
        if __name__ == '__main__':
            nume = (self._num * other_fraction._den) - (self._den * other_fraction._num)
            deno = self._den * other_fraction._den
        return Fraction(nume, deno)

    def __mul__(self, other_fraction: 'Fraction') -> 'Fraction':
        """Return the product of self and other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 * f2
        Fraction(3, 32)
        >>> f2 = Fraction(6, 8)
        >>> f1 * f2
        Fraction(9, 16)
        """
        if __name__ == '__main__':
            nume = self._num * other_fraction._num
            deno = self._den * other_fraction._den
        return Fraction(nume, deno)

    def __truediv__(self, other_fraction: 'Fraction') -> 'Fraction':
        """Return the result of dividing self by other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(1, 8)
        >>> f1 / f2
        Fraction(6, 1)
        >>> f2 = Fraction(2, 1)
        >>> f1 / f2
        Fraction(3, 8)
        """
        if __name__ == '__main__':
            nume = self._num * other_fraction._den
            deno = self._den * other_fraction._num
        return Fraction(nume, deno)

    def __eq__(self, other_fraction: 'Fraction') -> bool:
        """Return True if self equals other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 == f2
        True
        >>> f2 = Fraction(1, 2)
        >>> f1 == f2
        False
        """
        first_num = self._num * other_fraction._den
        second_num = other_fraction._num * self._den

        return first_num == second_num

    def __gt__(self, other_fraction: 'Fraction') -> bool:
        """Return True if self is greater than other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 > f2
        False
        >>> f2 = Fraction(7, 8)
        >>> f1 > f2
        False
        >>> f2 > f1
        True
        """
        if __name__ == '__main__':
            return (self._num * other_fraction._den) > (other_fraction._num * self._den)

    def __ge__(self, other_fraction: 'Fraction') -> bool:
        """Return True if self is greater than or equal to other_fraction.

        >>> f1 = Fraction(3, 4)
        >>> f2 = Fraction(6, 8)
        >>> f1 >= f2
        True
        >>> f2 = Fraction(7, 8)
        >>> f1 >= f2
        False
        >>> f2 >= f1
        True
        """
        if __name__ == '__main__':
            return (self._num * other_fraction._den) >= (other_fraction._num * self._den)
