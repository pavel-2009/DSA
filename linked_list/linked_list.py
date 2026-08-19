"""Linked list core realisation"""


class Node:
    def __init__(self, value: int, next: "Node | None" = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.last: Node | None = None

    def append_end(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.last = self.head
            return

        self.last.next = node
        self.last = node

    def append_start(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.last = self.head
            return

        node.next = self.head
        self.head = node

    def insert_after(self, current: Node, node: Node) -> None:
        pass

    def delete_start(self) -> None:
        pass

    def delete_end(self) -> None:
        pass

    def delete_after(self, current: Node) -> None:
        pass

    def find(self, value: int) -> Node | None:
        pass

    def contains(self, value: int) -> bool:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self):
        pass

    def __str__(self) -> str:
        pass