"""Linked list core realisation"""


class Node:
    def __init__(self, value: int, next: "Node | None" = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.last: Node | None = None
        self.len = 0

    def append_end(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.last = self.head
            self.len += 1
            return

        self.last.next = node
        self.last = node
        self.len += 1

    def append_start(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.last = self.head
            self.len += 1
            return

        node.next = self.head
        self.head = node
        self.len += 1

    def insert_after(self, current: Node, node: Node) -> None:
        if not current:
            return
        
        if not self.head:
            self.head = node
            self.last = self.head
            self.len += 1
            return

        if self.last == current:
            self.last = node

        node.next = current.next
        current.next = node
        self.len += 1

    def delete_start(self) -> None:
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.last = None
            self.len -= 1
            return

        self.head = self.head.next
        self.len -= 1

    def delete_end(self) -> None:
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.last = None
            self.len -= 1
            return

        current = self.head

        while current.next != self.last:
            current = current.next

        current.next = None
        self.last = current
        self.len -= 1

    def delete_after(self, current: Node) -> None:
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            self.last = None
            self.len -= 1
            return

        if not current.next:
            return

        current_ = self.head

        while current_ != current:
            if not current_.next:
                return None
            
            current_ = current_.next

        current_.next = current_.next.next
        self.len -= 1

    def find(self, value: int) -> Node | None:
        current = self.head

        while current:
            if current.value == value:
                return current

            current = current.next

        return None
            

    def contains(self, value: int) -> bool:
        return self.find(value) is not None

    def __len__(self) -> int:
        return self.len

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

    def __str__(self) -> str:
        values = []
        current = self.head

        while current:
            values.append(str(current.value))
            current = current.next

        return " -> ".join(values) + " -> None"