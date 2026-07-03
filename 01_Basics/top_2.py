data = [    {"product": "A", "sales": 100},
    {"product": "B", "sales": 200},
    {"product": "C", "sales": 150}]
top_products = sorted(data, key=lambda x: x["sales"], reverse=True)[:2]
print(top_products)
