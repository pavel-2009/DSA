"""Queue core realisation"""

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, value: int):
        self.in_stack.append(value)

    def pop(self):
        if not self.out_stack:  # Переносим только если out_stack пуст
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:  # Очередь пуста
            return None
        
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:  # Переносим только если out_stack пуст
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        if not self.out_stack:  # Очередь пуста
            return None
        
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


def process_commands(commands: list[str], queue: Queue):
    commands_available = {
        "push": queue.push,
        "pop": lambda: print(f"Popped: {queue.pop()}"),  # Для отладки
        "peek": lambda: print(f"Peek: {queue.peek()}")   # Для отладки
    }

    for command in commands:
        com_params = command.split(' ')
        if len(com_params) == 1:
            com = com_params[0]
            if com in commands_available:
                commands_available[com]()
            else:
                print(f"Unknown command: {com}")
        elif len(com_params) == 2:
            com, val = com_params
            if com in commands_available:
                commands_available[com](int(val))
            else:
                print(f"Unknown command: {com}")
        else:
            print("Unknown command")

    print(f"in_stack: {queue.in_stack}")
    print(f"out_stack: {queue.out_stack}")

if __name__ == '__main__':
    queue = Queue()

    commands = [
        "push 5",
        "push 10",
        "pop",
        "push 20",
        "pop",
    ]

    process_commands(commands, queue)