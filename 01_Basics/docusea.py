documents = [    "Python FastAPI Guide",    "React Tutorial",    "PostgreSQL Indexing"]
def search(query):
    result = []
    for doc in documents:
        if query.lower() in doc.lower():
            result.append(doc)
    return result
print(search("python"))
