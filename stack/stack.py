"""Stack core realisation"""

from typing import Optional


class Stack:
    def __init__(self):
        self.items_ = []

    def push(self, value: int):
        self.items_.append(value)

    def pop(self) -> Optional[int]:
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        return self.items_.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self._items[-1]

    def is_empty(self):
        return len(self.items_) == 0

    def size(self):
        return len(self.items_)
