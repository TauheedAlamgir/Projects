# Tauheed alamgir 101194927

# SYSC 2100 Lab 5

# An implementation of ADT Bag that uses a singly-linked list as the
# underlying data structure.

import random
from typing import Any

"""
History:
1.00 Feb. 13, 2022 - Initial release.
"""

class LinkedBag:

    class Node:
        def __init__(self, x: Any) -> None:
            """Construct a node containing payload x."""
            self.x = x
            self.next = None

    def __init__(self, iterable=[]) -> None:
        """Initialize this LinkedBag with the contents of iterable.

        If iterable isn't provided, the new bag is empty.

        >>> bag = LinkedBag()
        >>> bag
        LinkedBag()
        >>> bag = LinkedBag([1, 2, 3, 4])
        >>> bag
        LinkedBag([4, 3, 2, 1])
        """
        self._head = None
        self._n = 0  # No. of items in the bag.

        for item in iterable:
            self.add(item)  # add() updates self._n

    def __str__(self) -> str:
        """Return a string representation of this bag."""
        # Iterate over the linked list, building a (Python) list containing
        # the string representation of each element.
        items = []
        node = self._head
        while node is not None:
            items.append(repr(node.x))
            node = node.next
        return "[{0}]".format(", ".join(items))

    def __repr__(self) -> str:
        """Return the canonical string representation of this bag."""
        # Create a string such that eval(repr(obj)) yields an SLList that
        # is identical to obj.
        return "{0}({1})".format(self.__class__.__name__, str(self))

    def __len__(self) -> int:
        """Return the number of elements in this bag."""
        return self._n

    def _new_node(self, x: Any) -> 'LinkedBag.Node':
        """Return a node with payload x that can be linked into this bag."""
        return LinkedBag.Node(x)

    def add(self, item: Any) -> None:
        """Add item to this bag.

        The running time is O(1).

        >>> bag = LinkedBag()
        >>> for x in [3, 1, 2, 3, 4]:
        ...     bag.add(x)
        ...
        >>> len(bag)
        5
        >>> bag
        LinkedBag([4, 3, 2, 1, 3])
        """
        if len(self) == 0:
            self._n = self._n + 1
            self._head = self.Node(item)
        else:
            pointer = self.Node(item)
            pointer.next = self._head
            self._n = self._n + 1
            self._head = pointer

    def __contains__(self, item: Any) -> bool:
        """Return True if item is in the bag.

        The running time is O(n), worst case.

        >>> bag = LinkedBag()
        >>> 2 in bag
        False
        >>> bag = LinkedBag([1, 2, 3, 4])
        >>> 2 in bag
        True
        >>> 7 in bag
        False
        """
        count=0
        pointer = self._head
        while pointer != None:
            if pointer.x == item:
                count = count + 1
            pointer = pointer.next
        return count


    def count(self, item: Any) -> int:
        """Return the total number of occurrences of item in this bag.

        The running time is O(n).

        >>> bag = LinkedBag([3, 1, 2, 3, 4])
        >>> bag.count(2)
        1
        >>> bag.count(3)
        2
        >>> bag.count(5)
        0
        """
        count=0
        pointer = self._head
        while pointer != None:
            if pointer.x == item:
                count = count + 1
            pointer = pointer.next
        return count

    def remove(self, item: Any) -> Any:
        """Remove and return one instance of item from this bag.

        The running time is O(n), worst case.

        Raises KeyError if the bag is empty.
        Raises KeyError if item is not in the bag.

        >>> bag = LinkedBag([5, 1, 2, 5, 4])
        >>> bag.count(5)
        2
        len(bag)
        5
        >>> bag.remove(5)
        5
        >>> bag.count(5)
        1
        >>> len(bag)
        4
        """

    def grab(self) -> Any:
        """Remove and return a randomly-selected item from this bag.

        The running time is O(n), worst case.

        Raises KeyError if the bag is empty.

        >>> bag = LinkedBag([3, 1, 2, 3, 4])
        >>> len(bag)
        5
        >>> bag.grab()
        3     # (Note: 1 or 2 or 4 may be displayed instead of 3, depending on
              #  which item was removed.)
        >>> len(bag)
        4
        """
        randomnumber = random.randrange(len(self) - 1)
        self.remove(randomnumber)
        randomnumber = (len(self) - 1)
        return randomnumber
