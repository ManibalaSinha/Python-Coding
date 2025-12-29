class MinStack:
   def __init__(self):
      self.stack= []
      self.min_stack = []
   def push(self,x):
      self.stack.append(x)
      if not self.min_stack or x <= self.min_stack[-1]:
         self.min_stack.append(x)

   def pop(self):
      if not self.stack:
         return
      val = self.stack.pop()
      if val == self.min_stack[-1]:
         self.min_stack.pop()

   def top(self):
      return self.stack[-1]
   
   def getMin(self):
      return self.min_stack[-1]
   
stack = MinStack()

stack.push(4)
stack.push(9)
stack.push(2)

print(stack.top())#2
print(stack.getMin())#2

stack.pop()

print(stack.top())#9
print(stack.getMin())#4