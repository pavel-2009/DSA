"""Linked list core realisation"""

class Node:
    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node):
        self.head = head
        self.last = self.head

    def append_end(self, node: Node):
        if not self.head:
            self.head = node
            self.last = self.head
            return

        self.last.next = node
        self.last = self.last.nest

    def append_start(self, node: Node):
        if not self.head:
            self.head = node
            self.last = self.head
            return

        node.next = self.head
        self.head = node

    def append(self, node: Node, current: Node):
        if not self.head:
            self.head = node
            self.last = self.head
            return

        next_ = current.next.next
        current.next = node
        current.next.next = next_
