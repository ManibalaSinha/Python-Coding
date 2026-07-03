users = {
    "alice": ["admin"],
    "bob": ["editor"]
}

roles = {
    "admin": ["dashboard", "settings"],
    "editor": ["dashboard"]
}

def can_access(user, page):
   for user in users:
      print(user)
      for role in roles:
         pages= roles.get(role,[])
         if page in pages:
            return True         
      return False
print(can_access("alice","dashboard"))
print(can_access("bob","settings"))