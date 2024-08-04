from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,item):
        self.queue.appendleft(item)
    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue) == 0
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
print(queue.is_empty())
print(queue.queue)
print(queue.peek())
print(queue.size())