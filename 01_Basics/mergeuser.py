def merge_users(users):
    merged = {}
    for user in users:
        email = user["email"]
        if email not in merged:
            merged[email] = {}
        merged[email].update(user)
    return list(merged.values())
users = [{"email":"a@gmail.com","name":"John"},  {"email":"a@gmail.com","phone":"111"},    {"email":"b@gmail.com","name":"Alice"} ]

print(merge_users(users))
