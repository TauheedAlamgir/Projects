# Tauheed Alamgir 101194927

# SYSC 2100 Winter 2022 Lab 7

from typing import Any

class Node:
    """A node in a singly-linked list."""

    def __init__(self, node_data: Any) -> None:
        """Construct a Node with payload node_data. The node's link is
        initialized with the end-of-list marker.
        """
        self.data = node_data
        self._next = None

    def __str__(self) -> str:
        """Return a string representation of the payload in this Node."""
        return str(self.data)

    def __repr__(self) -> str:
        """Return a string representation of this Node."""
        return 'Node({0})'.format(repr(self.data))


def build_linked_list(lst: list) -> Node:
    """Build a singly-linked list containing the elements in lst, and return a
    reference to the first node.

    >>> head = build_linked_list([10, 20, 30, 40])
    >>> to_string(head)
    '10 -> 20 -> 30 -> 40'
    """
    head = None
    # Traverse lst back to front
    for i in range(len(lst) - 1, -1, -1):
        # insert a node (3-step link-in)
        node = Node(lst[i])
        node._next = head
        head = node
    return head


def to_string(head: Node) -> str:
    """Return a string representation of the linked list referred to by head.

    >>> head = build_linked_list([10, 20, 30, 40])
    >>> to_string(head)
    '10 -> 20 -> 30 -> 40'
    """
    if head is None:
        return 'None'

    node = head
    # Traverse the linked list from head to tail, collecting the data
    # in the nodes as a (Python) list of strings.
    items = []
    while node is not None:
        items.append(repr(node.data))
        node = node._next

    # Concatenate the strings in items, with each pair separated by " -> "
    return " -> ".join(items)

# --------------------------------
# Exercise 1


def power(x: float, n: int) -> float:
    """Return x raised to the power n.

    Precondition: n >= 0.

    >>> power(3.5, 0)
    1.0
    >>> power(3.5, 1)
    3.5
    >>> power(3.5, 2)
    12.25
    """
    if (n == 0):
        return 1.0
    elif(n == 1):
        return x
    else:
        return (x * power(x, n-1))

# --------------------------------
# Exercise 2


def num_digits(n: int) -> int:
    """Return the number of digits in n.

    Precondition: n >= 0.

    >>> num_digits(492)
    3
    >>> num_digits(63)
    2
    >>> num_digits(7)
    1
    """
    if (n // 10 == 0):
        return 1
    else:
        return 1 + num_digits(n // 10)

# --------------------------------
# Exercise 3


def count(head: Node, x: Any) -> int:
    """Return the total number of occurrences of x in the linked list
    referred to by head.

    >>> head = None
    >>> count(head, 5)
    0
    >>> head = build_linked_list([10, 20, 10, 30, 20, 10])
    >>> to_string(head)
    '10 -> 20 -> 10 -> 30 -> 20 -> 10'
    >>> count(head, 10)
    3
    >>> count(head, 30)
    1
    """
    if (head == None):
        return 0
    elif(head.data == x):
        return 1 + count(head._next, x)
    else:
        return count(head._next, x) 

# --------------------------------
# Exercise 4


def last(head: Node) -> Any:
    """Return the last integer in the linked list referred to by head.

    Precondition: head is not None (the linked list is not empty).

    >>> head = build_linked_list([1, 2, 4, 4, 6, 5])
    >>> to_string(head)
    '1 -> 2 -> 4 -> 4 -> 6 -> 5'
    >>> last(head)
    5
    >>> head = build_linked_list([10])
    >>> to_string(head)
    '10'
    >>> last(head)
    10
    """
    if (head._next == None):
        return head.data
    else:
        return last(head._next)

# --------------------------------
# Exercise 5


def copy(head: Node) -> Node:
    """Make a copy of the linked list referred to by head (duplicate
    all the nodes in the original list) and return a reference to the
    first node in the new linked list.

    >>> head = build_linked_list([1, 2, 4, 4, 6, 5])
    >>> to_string(head)
    '1 -> 2 -> 4 -> 4 -> 6 -> 5'
    >>> copied = copy(head)
    >>> to_string(copied)
    '1 -> 2 -> 4 -> 4 -> 6 -> 5'
    """
    if (head == None):
        return None
    else:
        tempHead = Node(head.data)
        tempHead._next = (copy(head._next))
        return tempHead
