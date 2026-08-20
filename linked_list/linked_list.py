"""Linked list core realisation"""

from typing import Optional


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

        if not current or not current.next:
            return

        current_ = self.head

        while current_ != current:
            if not current_.next:
                return None
            
            current_ = current_.next

        if current_.next == self.last:
            self.last = current_

        current_.next = current_.next.next
        self.len -= 1

    def find(self, value: int) -> Optional[Node]:
        current = self.head

        while current:
            if current.value == value:
                return current

            current = current.next

        return None
            

    def contains(self, value: int) -> bool:
        return self.find(value) is not None

    def reverse(self):
        prev = None
        current = self.head

        self.last = self.head

        while current:
            next_ = current.next
            current.next = prev

            prev = current
            current = next_

        self.head = prev

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


def main():
    linked_list = LinkedList()

    # 1. Создаём узлы
    node_10 = Node(10)
    node_20 = Node(20)
    node_30 = Node(30)
    node_40 = Node(40)

    # 2. Добавляем в конец
    linked_list.append_end(node_10)
    linked_list.append_end(node_20)
    linked_list.append_end(node_30)

    print("После append_end:")
    print(linked_list)
    print("Длина:", len(linked_list))
    print()

    linked_list.reverse()
    print("После разворота")
    print(linked_list)

    # 3. Добавляем в начало
    linked_list.append_start(node_40)

    print("После append_start:")
    print(linked_list)
    print()

    # 4. Вставляем после конкретного узла
    node_50 = Node(50)
    linked_list.insert_after(node_20, node_50)

    print("После insert_after(20, 50):")
    print(linked_list)
    print()

    # 5. Поиск
    found = linked_list.find(30)

    print("find(30):", found.value if found else None)
    print("contains(100):", linked_list.contains(100))
    print("contains(30):", linked_list.contains(30))
    print()

    # 6. Удаляем первый элемент
    linked_list.delete_start()

    print("После delete_start:")
    print(linked_list)
    print()

    # 7. Удаляем последний элемент
    linked_list.delete_end()

    print("После delete_end:")
    print(linked_list)
    print()

    # 8. Удаляем элемент после конкретного узла
    current = linked_list.find(20)

    if current:
        linked_list.delete_after(current)

    print("После delete_after(20):")
    print(linked_list)
    print()

    # 9. Проверяем итерацию
    print("Итерация по списку:")

    for node in linked_list:
        print(node.value)

    print()

    # 10. Проверяем head и last
    print("Head:", linked_list.head.value if linked_list.head else None)
    print("Last:", linked_list.last.value if linked_list.last else None)
    print("Length:", len(linked_list))


if __name__ == "__main__":
    main()