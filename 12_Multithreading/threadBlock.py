import threading
from collections import deque

class BlockingQueue:
    def __init__(self, capacity):
        self.queue = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def put(self, item):
        with self.not_full:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(item)
            self.not_empty.notify()

    def get(self):
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()
            item = self.queue.popleft()
            self.not_full.notify()
            return item
