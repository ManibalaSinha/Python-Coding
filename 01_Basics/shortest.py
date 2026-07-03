from collections import deque

def shortest_path(graph, start):
    queue = deque([start])
    dist = {start: 0}

    while queue:
        node = queue.popleft()

        for nei in graph[node]:
            if nei not in dist:
                dist[nei] = dist[node] + 1
                queue.append(nei)

    return dist
print(shortest_path({  0: [1,2],  1: [0,3],  2: [0,3],  3: [1,2]},0))