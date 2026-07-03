roles = {
    "admin": {
        "inherits": ["viewer"],
        "pages": ["settings"]
    },
    "viewer": {
        "inherits": [],
        "pages": ["dashboard"]
    }
}
#recursion
def get_permission(role):
   role_data = roles[role]
   perm = set(role_data["inherits"])
   for inherited in role_data:
      perm.update(get_permission(inherited))
      return perm
print(roles["admin"])