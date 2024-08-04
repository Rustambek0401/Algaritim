class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
        return self.items

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            self.items.pop()
            return self.items
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)
print(stack.push(55))
print(stack.pop())
