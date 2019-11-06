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