def removeStars(s):
   stack=[]
   for ch in s:
      if ch == "*":
         if stack:
            stack.pop()
      else:
         stack.append(ch)
   return "".join(stack)
print(removeStars("leet**cod*e"))
