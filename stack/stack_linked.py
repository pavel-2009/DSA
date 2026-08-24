"""Stack core realisation based on linked list"""

from typing import Optional

from linked_list.linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.items_ = LinkedList()

    def push(self, value: int):
        node = Node(value)
        self.items_.append_start(node)
    
    def pop(self) -> Optional[int]:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")

        result = self.items_.head.value
        self.items_.delete_start()

        return result

    def peek(self) -> Optional[int]:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        result = self.items_.head.value

        return result
    
    def is_empty(self) -> bool:
        return self.items_.head != None

    def size(self) -> int:
        return len(self.items_)
    