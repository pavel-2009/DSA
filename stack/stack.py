"""Stack core realisation"""


class Stack:
    def __init__(self):
        self.items_ = []

    def push(self, value: int):
        self.items_.append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        return self.items_.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("peek from empty stack")

        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self.items_) == 0

    def size(self) -> int:
        return len(self.items_)
