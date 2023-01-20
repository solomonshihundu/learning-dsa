from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def populate(self,max):
        for i in range(0,max):
            self.enqueue(i)

    def print(self):
        print(self.buffer)


pq = Queue()
pq.populate(10)
pq.print()
print(pq.size())
pq.dequeue()
print(pq.size())


