def countComponents(n, edges):
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parent[find(x)] = find(y)
    
    for u, v in edges:
        union(u, v)
    
    return len({find(x) for x in range(n)})
