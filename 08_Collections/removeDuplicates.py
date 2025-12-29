def remove_duplicates(lst:list) -> list:
   seen = set()
   result = []
   for x in lst:
      if x not in seen:
         seen.add(x)
         result.append(x)
   return result
print(remove_duplicates([2,3,2,3,3,2]))