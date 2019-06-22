class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)
        return True
    
    def pop(self, v):
        if self.is_empty():
            return False
        return self.pop()

    def is_empty(self):
        return bool(self.stack)

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return bool(self.stack)

    def add(self, item):
        self.queue.append(item)
        return True

    def remove(self):
        if self.is_empty():
            return False
        self.queue = self.queue[1:]
        return True

    def peek(self ):
        if self.is_empty():
            return None
        return self.queue[0]