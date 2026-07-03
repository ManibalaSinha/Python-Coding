users = {
    "alice": ["admin"],
    "bob": ["viewer"]
}

roles = {
    "admin": ["dashboard", "settings", "reports"],
    "viewer": ["dashboard"]
}
def can_access(user,page):
   user_roles= users.get(user, [])
   for role in user_roles:
      pages= roles.get(role, [])
      if page in pages:
         return True
   return False
print(can_access("admin","dashboard"))