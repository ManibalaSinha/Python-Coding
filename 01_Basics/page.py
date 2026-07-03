users = {
    "alice": ["admin"],
    "bob": ["viewer"]
}

roles = {
    "admin": ["dashboard", "settings"],
    "viewer": ["dashboard"]
}
def has_permi(user, page):  
   user_roles = users.get(user, [])
   for role in user_roles:
      permissions = roles.get(role, [])
      if page in permissions:
         return True
   return False