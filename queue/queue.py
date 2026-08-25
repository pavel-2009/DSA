"""Queue core realisation"""

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, value: int):
        self.in_stack.append(value)

    def pop(self):
        if self.in_stack:
            for _ in range(len(self.in_stack)):
                last = self.in_stack.pop()
                self.out_stack.append(last)

        return self.out_stack.pop()

    def peek(self):
        if self.in_stack:
            for _ in range(len(self.in_stack)):
                last = self.in_stack.pop()
                self.out_stack.append(last)

        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


def process_commands(commands: list[str], queue: Queue):
    commands_available = {
        "push": queue.push,
        "pop": queue.pop
    }

    for command in commands:
        com_params = command.split(' ')
        if len(com_params) == 1:
            com = com_params[0]
            commands_available[com]()
        elif len(com_params) == 2:
            com, val = com_params
            commands_available[com](val)
        else:
            print("Unknown command")

    print(queue.in_stack)
    print(queue.out_stack)

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
