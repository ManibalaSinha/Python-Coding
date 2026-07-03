from collections import deque
import time
class RateLimiter:
    def __init__(self):
        self.requests = deque()
    def allow(self):
        now = time.time()
        while self.requests and now - self.requests[0] > 60:
            self.requests.popleft()
        if len(self.requests) < 3:
            self.requests.append(now)
            return True
        return False
