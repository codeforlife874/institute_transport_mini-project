import sys
from campus_data import EDGES, get_all_locations

def find_all_paths(u, d, visited, path, graph, current_cost):
    visited[u] = True
    path.append(u)

    if u == d:
        print(f"Path: {path}, Cost: {current_cost}, Stops: {len(path)-1}")
    else:
        for i, weight in graph[u]:
            if not visited[i]:
                find_all_paths(i, d, visited, path, graph, current_cost + weight)

    path.pop()
    visited[u] = False

def test():
    from collections import defaultdict
    graph = defaultdict(list)
    for u, v, w in EDGES:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    num_nodes = max(max(u, v) for u, v, w in EDGES) + 1
    visited = [False] * num_nodes
    find_all_paths(2, 26, visited, [], graph, 0)

if __name__ == "__main__":
    test()
