company = {
    "teams": [
        {
            "name": "backend",
            "users": [
                {"name": "alice"},
                {"name": "bob"}
            ]
        },
        {
            "name": "frontend",
            "users": [
                {"name": "john"}
            ]
        }
    ]
}
for team in company["teams"]:
   #print(team["name"])
   for user in team["users"]:
      print(user['name'])