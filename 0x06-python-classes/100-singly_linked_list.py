#!/usr/bin/python3
"""Defines a class Node for a singly linked list."""


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): The next node in the linked list, or None if this is the last node.

    """
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node object.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the linked list, or None if this is the last node.

        Raises:
            TypeError: If data is not an integer.

        """
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node or None): The first node in the linked list, or None if the list is empty.

    """
    def __init__(self):
        """
        Initialize a new SinglyLinkedList object.

        """
        self.head = None

    def __str__(self):
        """
        Return a string representation of the linked list.

        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the correct sorted position in the list.

        Args:
            value (int): The value to be stored in the new node.

        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
