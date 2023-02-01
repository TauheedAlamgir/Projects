# Tauheed Alamgir 101194927


"""Class BinarySearchTree implements the binary search tree from Section 6.2
of 'Open Data Structures (in pseudocode)', Edition 0.1G Beta.
"""

from typing import Any

class BinarySearchTree:

    class Node:
        def __init__(self, x: Any) -> None:
            """Construct a node with no parent and no children,
            containing key x.
            """
            self._x = x
            self._parent = None
            self._left = None
            self._right = None

    def __init__(self, iterable = []) -> None:
        """Initialize this BinarySearchTree with the contents of iterable.
        Duplicate keys in iterable are not inserted in the BST.

        If iterable isn't provided, the new BST is empty.
        """
        self._root = None
        self._n = 0  # Number of nodes in the BST

        for key in iterable:
            self.add(key)  # add() updates self._n

    def size(self) -> int:
        """Return the number of nodes in this BST."""
        return self._n

    def find_eq(self, x: Any) -> Any:
        """If key x is in this BinarySearchTree, return the key; otherwise
        return None.
        """
        w = self._root
        while w != None:
            if x < w._x:
                w = w._left
            elif x > w._x:
                w = w._right
            else:
                return w._x
        return None

    def find(self, x: Any) -> Any:
        """If key x is in this BinarySearchTree, return the key; otherwise
        return the smallest value in the BST that is greater than x. If
        no key in the BST is greater than or equal to x, return None.
        """
        w = self._root
        z = None
        while w != None:
            if x < w._x:
                z = w
                w = w._left
            elif x > w._x:
                w = w._right
            else:
                return w._x
        if z == None:
            return None
        return z._x

    def add(self, x: Any) -> bool:
        """If key x is not in this BinarySearchTree, insert x and return True;
        otherwise return False.
        """
        p = self._find_last(x)
        return self._add_child(p, BinarySearchTree.Node(x))

    def _find_last(self, x: Any) -> Node:
        """If key x is in this BinarySearchTree, return the reference to the
        node that contains x.
        If key x is not in the BST, return the reference to the node that will
        become the parent of a new node containing x.
        If the BST is empty, return None.
        """
        w = self._root
        prev = None
        while w != None:
            prev = w
            if x < w._x:
                w = w._left
            elif x >= w._x:
                w = w._right
            else:
                return w
        return prev

    def _add_child(self, p: Node, u: Node) -> bool:
        """If p is None, the BST is empty, so install u as the root node.

        If the BST is not empty, insert node u as the left or right child of
        node p, such that the binary search tree property is maintained,
        and return True.

        If key u.x is already in the BST, return False (the BST is not
        modified).
        """
        if p == None:
            self._root = u
        else:
            if u._x < p._x:
                p._left = u
            elif u._x >= p._x:
                p._right = u
            else:
                return False
            u._parent = p
        self._n = self._n + 1
        return True

    def remove(self, x: Any) -> bool:
        """If key x is in this BinarySearchTree, remove it and return True;
        otherwise return False.
        """
        u = self._find_last(x)
        if u != 0 and x == u._x:
            self._remove_node(u)
            return True
        return False
    
    def _remove_node(self, u: Node) -> None:
        """Remove node u from this BinarySearchTree, such that the binary
        search tree property is maintained.
        """
        if u._left == None or u._right == None:
            self._splice(u)
        else:
            w = u._right
            while w._left == None:
                w = w._left
            u._x = w._x
            self._splice(w)

    def _splice(self, u: Node) -> None:
        """Remove node u from this BinarySearchTree.

        Precondition: u is a leaf or has one child.
        """
        if u._left != None:
            s = u._left
        else:
            s = u._right
        if u == self._root:
            self._root = s
            p = None
        else:
            p = u._parent
            if p._left == u:
                p._left = s
            else:
                p._right = s
        if s != None:
            s._parent = p
        self._n = self._n - 1

    def preorder_print(self) -> None:
        """Print this BST using a preorder traversal."""
        self._preorder_print(self._root)

    def _preorder_print(self, node: Node) -> None:
        """Print the BST rooted at node using a preorder traversal."""
        if node is None:
            return
        print(node._x)
        self._preorder_print(node._left)
        self._preorder_print(node._right)

    def inorder_print(self) -> None:
        """Print this binary tree using an inorder traversal."""
        self._inorder_print(self._root)

    def _inorder_print(self, node: Node) -> None:
        """Print the binary tree rooted at node using an inorder traversal."""
        if node is None:
            return
        self._inorder_print(node._left)
        print(node._x)
        self._inorder_print(node._right)

    def postorder_print(self) -> None:
        """Print this binary tree using a postorder traversal."""
        self._postorder_print(self._root)

    def _postorder_print(self, node: Node) -> None:
        """Print the binary tree rooted at node using a postorder traversal."""
        if node is None:
            return
        self._postorder_print(node._left)
        self._postorder_print(node._right)
        print(node._x)
