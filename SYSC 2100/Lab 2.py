# Tauheed Alamgir 101194927

# SYSC 2100 Lab 2
# Last edited: Jan. 22, 2022

# An implementation of ADT Bag that uses Python's list type as the
# underlying data structure.

from typing import Any
import random

class ListBag:

    def __init__(self, iterable=None) -> None:
        """Initialize this ListBag with the contents of iterable.

        If iterable isn't provided, the new bag is empty.

        >>> bag = ListBag()
        >>> bag
        ListBag()
        >>> bag = ListBag([1, 2, 3, 4])
        >>> bag
        ListBag([1, 2, 3, 4])
        """
        self._elems = []
        if iterable is not None:
            for item in iterable:
                self._elems.append(item)

    def __str__(self) -> str:
        """Return a string representation of this bag.

        >>> bag = ListBag()
        >>> str(bag)
        '<>'
        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> str(bag)
        '<3, 1, 2, 3, 4>'
        """
        if len(self._elems) == 0:
            return '<>'
        else:
            # Use repr(x) instead of str(x) in the list comprehension so that
            # elements of type str are enclosed in quotes.
            return "<{0}>".format(", ".join([repr(x) for x in self._elems]))

            # The above statement is equivalent to this code:
            # Form a string containing the elements in the bag, with the format:
            # '<elem1, elem2, elem3, ...>'
            #
            # tmp = []
            # for x in self._elems:
            #     tmp.append(repr(x))
            # s = ''
            # for i in range(len(tmp)):
            #    s += tmp[i]
            #    #  Append a trailing comma after all but the last element
            #    if i < len(tmp) - 1:
            #        s += ', '
            # return "<{0}>".format(s)

    def __repr__(self) -> str:
        """Return a string representation of this bag.

        >>> bag = ListBag()
        >>> repr(bag)
        'ListBag()'
        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> repr(bag)
        'ListBag([3, 1, 2, 3, 4])'
        """
        if len(self._elems) == 0:
            return 'ListBag()'
        else:
            return 'ListBag({0})'.format(self._elems)

    def __iter__(self) -> "list_iterator":
        """Return an iterator for this bag.

        >>> bag = ListBag([1, 2, 3, 4])
        >>> for x in bag:
        ...     print(x)
        ...
        1
        2
        3
        4
        """
        return iter(self._elems)

    def __len__(self) -> int:
        """Return the number of items in this bag.

        >>> bag = ListBag()
        >>> len(bag)
        0
        >>> bag = ListBag([1, 2, 3, 4])
        >>> len(bag)
        4
        """
        return len(self._elems)

    def __contains__(self, item: Any) -> bool:
        """Return True if item is in the bag.

        >>> bag = ListBag()
        >>> 2 in bag
        False
        >>> bag = ListBag([1, 2, 3, 4])
        >>> 2 in bag
        True
        >>> 7 in bag
        False
        """
        return item in self._elems

    def count(self, item: Any) -> int:
        """Return the total number of occurrences of item in this bag.

        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> bag.count(2)
        1
        >>> bag.count(3)
        2
        """
        return self._elems.count(item)

    def add(self, item: Any) -> None:
        """Add item to this bag.

        >>> bag = ListBag()
        >>> for x in [3, 1, 2, 3, 4]:
        ...     bag.add(x)
        ...
        >>> len(bag)
        5
        >>> bag.count(1)
        1
        >>> bag.count(2)
        1
        >>> bag.count(3)
        2
        >>> bag.count(4)
        1
        """
        return self._elems.append(item)

    def remove(self, item: Any) -> Any:
        """Remove and return one instance of item from this bag.

        Raises KeyError if the bag is empty.
        Raises ValueError if item is not in the bag.

        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> bag.count(3)
        2
        len(bag)
        5
        >>> bag.remove(3)
        3
        >>> bag.count(3)
        1
        >>> len(bag)
        4
        """
        if len(self) == 0:
            raise KeyError("bag.remove(x): remove from empty bag")
        if not(item in self):
            raise ValueError("bag.remove(x): x not in bag")
        else:
            self._elems.remove(item)
            return item

    def grab(self) -> Any:
        """Remove and return a randomly selected item from this bag.

        Raises KeyError if the bag is empty.

        >>> bag = ListBag([3, 1, 2, 3, 4])
        >>> len(bag)
        5
        >>> bag.grab()
        3     # (Note: 1 or 2 or 4 may be displayed instead of 3, depending on
              #  which item was removed.)
        >>> len(bag)
        4
        """
        if len(self) == 0:
            raise KeyError("bag.grab(): grab from empty bag")
        else:
            return random.choice(self._elems)
        
        
