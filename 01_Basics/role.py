users = {
    "alice": ["admin", "editor"],
    "bob": ["viewer"]
}
roles = {
    "admin": ["read", "write", "delete"],
    "editor": ["read", "write"],
    "viewer": ["read"]
}
def has_permission(user, permission):
   user_roles= users.get(user, [])
   for role in user_roles:
      permissions = roles.get(role, [])
      if permission in permissions:
         #print(permission)
         return True
   return False
print(has_permission("alice","write"))

      
      