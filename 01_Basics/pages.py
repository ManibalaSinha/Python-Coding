users = {
    "alice": ["admin"],
    "bob": ["viewer"]
}

roles = {
    "admin": ["dashboard", "settings"],
    "viewer": ["dashboard"]
}
def get_pages(user):
   pages =set()
   for role in users.get(user,[]):
      for page in roles.get(role,[]):
         pages.add(page)
   return list(page)
print(get_pages("alice"))

