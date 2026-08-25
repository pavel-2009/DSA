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
