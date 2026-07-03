files = [{"name":"a.pdf","size":100}, {"name":"b.pdf","size":300},{"name":"c.pdf","size":200}]
def largest_file(files):
    if not files:
        return None
    return max(files, key=lambda f: f["size"])
print(largest_file(files))
