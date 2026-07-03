class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.q:
            return self.q.pop(0)
        return -1

    def front(self):
        return self.q[0] if self.q else -1

    def is_empty(self):
        return len(self.q) == 0
q = Queue()# Ex
q.enqueue(1) 
q.enqueue(2)
q.enqueue(3)
print(q.dequeue()) #1
print(q.front()) #2
print(q.is_empty())
