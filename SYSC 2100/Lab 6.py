# Tauheed Alamgir 101194927

# SYSC 2100 Lab 6/Assignment 1

# An implementation of ADT Polynomial that uses a singly-linked list as the
# underlying data structure.

# A polynomial consists of 0 or more terms, with each term consisting of a
# coefficient and an exponent. Coefficients are integers, and terms with zero
# coefficients are not stored in the linked list. Exponents are non-negative
# integers.

from typing import Any

"""
History:
1.00 Feb. 21, 2022 - Initial release.
"""

class Polynomial:

    class TermNode:
        def __init__(self, coefficient: int, exponent: int) -> None:
            """Initialize this node to represent a polynomial term with the
            given coefficient and exponent.

            Raise ValueError if the coefficent is 0 or if the exponent
            is negative.
            """
            if coefficient == 0:
                raise ValueError("TermNode: zero coefficient")
            if exponent < 0:
                raise ValueError("TermNode: negative exponent")

            self.coeff = coefficient
            self.exp = exponent
            self.next = None

    def __init__(self, coefficient: int = None, exponent: int = 0) -> None:
        """Initialize this Polynomial with a single term constructed from the
        coefficient and exponent.

        If one argument is given, the term is a constant coefficient
        (the exponent is 0).
        If no arguments are given, the Polynomial has no terms.

        # Polynomial with no terms:
        >>> p = Polynomial()
        >>> print(p._head)
        None
        >>> print(p._tail)
        None

        # Polynomial with one term (a constant):
        >>> p = Polynomial(12)
        >>> p._head.coeff
        12
        >>> p._head.exp
        0
        >>> print(p._head.next)
        None

        # Polynomial with one term:
        >>> p = Polynomial(12, 2)
        >>> p._head.coeff
        12
        >>> p._head.exp
        2
        >>> print(p._head.next)
        None
        """
        # A polynomial is stored as a singly linked list. Each node stores
        # one term, with the nodes ordered in descending order, based on the
        # exponent. (The head node is the term with the highest exponent,
        # and the tail node is the term with the lowest exponent.)
        if coefficient is None and exponent == 0:
            self._head = None
        else:
            self._head = Polynomial.TermNode(coefficient, exponent)
        self._tail = self._head

    def __str__(self) -> str:
        """Return a string representation of this polynomial.

        # Polynomial with no terms:
        >>> p = Polynomial()
        >>> str(p)
        ''

        # Polynomial with one term (a constant):
        >>> p = Polynomial(12)
        >>> str(p)
        '12'

        # Polynomials with one term:
        >>> p = Polynomial(12, 1)
        >>> str(p)
        '12x'

        >>> p = Polynomial(12, 2)
        >>> str(p)
        '12x^2'

        # See __add__ for string representations of polynomials with
        # more than one term.
        """
        x = ""
        y = self._head
        while y != None:                
            if len (x) > 0:                 
                x = x + " + "  
            x = x + str (y.coeff)
            if y.exp == 1:
                x = x + "x"
            elif y.exp > 0:              
                x = x + "x^" + str (y.exp)   
            y = y.next 
        return x

    def __repr__(self) -> str:
        """Return the same string as __str__."""
        return str(self)

    def degree(self) -> int:
        """Return this polynomial's degree.

        Raise ValueError if the polynomial has no terms.

        >>> p = Polynomial(12, 2)
        >>> p.degree()
        2
        """
        if self._head is None :
            return -1
        else :
            return self._head.exp

    def evaluate(self, x: float) -> float:
        """Evaluate the polynomial at x and return the result.

        Raise ValueError if the polynomial has no terms.

        >>> p = Polynomial(12, 2)
        >>> p.evaluate(3)
        108.0
        """
        t = self._head
        y = 0
        if t == None:
            raise ValueError("evaluate hasn't been implemented.")
        while t is not None:
            y = y + float(t.coeff * x ** (t.exp))
            t = t.next
        return y

    def __add__(self, rhs: 'Polynomial') -> 'Polynomial':
        """ Return a new Polynomial containing the sum of this polynomial
        and rhs.

        Raise ValueError if either polynomial has no terms.

        >>> p1 = Polynomial(12, 2)
        >>> p2 = Polynomial(-3, 1)
        >>> p3 = Polynomial(7)
        >>> p1 + p2
        12x^2-3x

        >>> p1 + p3
        12x^2+7

        >>> p1 + p2 + p3  # Equivalent to (p1 + p2) + p3
        12x^2-3x+7

        >>> p2 = Polynomial(3, 1)
        >>> p1 + p2 + p3
        12x^2+3x+7
        """
        raise NotImplementedError("__add__ hasn't been implemented.")

    def __mul__(self, rhs: 'Polynomial') -> 'Polynomial':
        """ Return a new Polynomial containing the product of this polynomial
        and rhs.

        Raise ValueError if either polynomial has no terms.

        >>> p1 = Polynomial(12, 2)
        >>> p2 = Polynomial(-3, 1)
        >>> p3 = Polynomial(7)
        >>> poly = p1 + p2 + p3
        >>> poly
        12x^2-3x+7

        >>> p4 = Polynomial(2, 1)
        >>> p4 * poly
        24x^3-6x^2+14x
        """
        raise NotImplementedError("__mul__ hasn't been implemented.")
