def valid_paren(s):
   stack =[]
   mapping = {")":"(","}":"{","]":"["}
   for c in s:
      if c in mapping.values():
         stack.append(c)
      elif c in mapping:
         if not stack or stack.pop()!= mapping[c]:
            return False
   return not stack