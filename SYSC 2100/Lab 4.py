# Tauheed Alamgir 101194927

from typing import Any
from collections import deque
import ctypes
import builtins

"""
History:
1.00 Feb. 6, 2022 - Initial release.
"""
class BoundedPriorityQueue:

    # DO NOT MODIFY __init__, __str__, __repr__ and __len__.

    def __init__(self, num_levels: int) -> None:
        """Initialize this BoundedPriorityQueue with priority levels
        ranging from 0 to num_levels - 1.

        >>> pq = BoundedPriorityQueue(6)
        >>> pq
        BoundedPriorityQueue(6)
        >>> str(pq)
        '<>'
        >>> len(pq)
        0
        """
        if num_levels <= 0:
            raise ValueError("_init_: num_levels <= 0")

        self._n = 0  # of elements stored in the priority queue
        # Allocate a fixed-capacity array of FIFO queues. All items with
        # priority k will be stored in self._queues[k] in FIFO order.
        self._queues = _new_array(num_levels)
        for i in range(num_levels):
            self._queues[i] = deque()

    def __str__(self) -> str:
        """Return a string representation of this BoundedPriorityQueue."""
        # Iterate over the array of FIFO queues, building a list of tuples,
        # with each tuple containing one element and its priority level,
        # arranged from the highest priority to the lowest.
        # If multiple elements have the same priority, they are arranged in
        # FIFO order.
        items = []
        for i in range(len(self._queues)):
            for elem in self._queues[i]:
                items.append((i, elem))
        return "<{0}>".format(", ".join([str(x) for x in items]))

    def __repr__(self) -> str:
        """Return a string representation of this BoundedPriorityQueue."""
        return "{0}({1})".format(self.__class__.__name__,
                                 str(len(self._queues)))

    def __len__(self) -> int:
        """Return the number of elements in this BoundedPriorityQueue."""
        return self._n

    def add(self, item: Any, priority: int) -> None:
        """Insert the specified item in this BoundedPriorityQueue,
        with the specified priority.

        Priority 0 is the highest priority.

        Raise ValueError if the priority level is not valid.

        >>> pq = BoundedPriorityQueue(6)
        >>> pq.add("purple", 5)
        >>> pq.add("black", 0)
        >>> pq.add("orange", 3)
        >>> pq.add("white", 0)
        >>> pq.add("green", 1)
        >>> pq.add("yellow", 5)
        >>> str(pq)
        "<(0, 'black'), (0, 'white'), (1, 'green'), (3, 'orange'), (5, 'purple'), (5, 'yellow')>"

        >>> pq.add("blue", 6)
        builtins.ValueError: add(item, priority): 6 is an invalid priority level
        """
        if (priority >= len(self._queues)):
            raise builtins.ValueError("add(" + item + "," +str(priority)  + "): " +str(priority) + " is an invalid priority level")
        else:
            self._queues[priority].append(item)
            self._n = self._n + 1

    def remove(self) -> Any:
        """ Remove and return the next item from this BoundedPriorityQueue.

        Raise an IndexError if the queue is empty.

        >>> pq = BoundedPriorityQueue(6)
        >>> pq.add("purple", 5)
        >>> pq.add("black", 0)
        >>> pq.add("orange", 3)
        >>> pq.add("white", 0)
        >>> pq.add("green", 1)
        >>> pq.add("yellow", 5)

        >>> while len(pq) > 0:
        ...     print(pq.remove())
        ...
        black
        white
        green
        orange
        purple
        yellow

        >>> pq.remove()
        builtins.IndexError: remove from an empty BoundedPriorityQueue
        """
        if(len(self) == 0):
            raise builtins.IndexError("remove from an empty BoundedPriorityQueue")
        else:
            for t in range(len(self._queues)):
                if(self._queues[t]): 
                    self._n = self._n - 1  
                    return self._queues[t].popleft()


# Pat's new_array function uses numpy. We're using Python's ctypes module,
# so that students don't have to install numpy.

def _new_array(capacity: int) -> 'py_object_Array_<capacity>':
    """Return a new array with the specified capacity that stores
    references to Python objects.
    """
    if capacity <= 0:
        raise ValueError('new_array: capacity must be > 0')
    PyCArrayType = ctypes.py_object * capacity
    a = PyCArrayType()
    for i in range(len(a)):
        a[i] = None
    return a

