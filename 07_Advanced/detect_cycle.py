def has_cycle(head):
   slow = fast = head
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
         return True
      return False
print(has_cycle([1,3,6,8]))