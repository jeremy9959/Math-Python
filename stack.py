class Stack:
    "a simple stack data structure based on a list"

    def __init__(self):
        self._stack = []

    def push(self, item):
        "push an item onto the stack"
        self._stack.append(item)

    def pop(self):
        "pop an item off the stack"
        if len(self._stack) == 0:
            raise IndexError("pop from empty stack")
        return self._stack.pop()

    def __len__(self):
        return len(self._stack)

    def reset(self):
        self._stack = []
