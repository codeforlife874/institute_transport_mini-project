# algorithms.py
# Shortest path algorithms: Dijkstra, BFS, A*

import heapq
from collections import deque

# ─────────────────────────────────────────────────────────
#  DIJKSTRA'S ALGORITHM  (Weighted Shortest Path)
# ─────────────────────────────────────────────────────────
def dijkstra(graph, source, destination):
    """
    Finds shortest path between source and destination using Dijkstra's Algorithm.
    Works on weighted graphs (distances in meters).
    
    Returns:
        path  : list of node IDs from source to destination
        dist  : total distance in meters
        visited_order : order in which nodes were explored (for visualization)
    """
    INF = float('inf')
    num_nodes = max(graph.get_all_nodes()) + 1

    distance = [INF] * num_nodes
    distance[source] = 0
    parent = [-1] * num_nodes
    visited = [False] * num_nodes
    visited_order = []

    # Min-heap: (distance, node)
    min_heap = [(0, source)]

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        visited[u] = True
        visited_order.append(u)

        if u == destination:
            break

        for v, weight in graph.get_neighbors(u):
            if not visited[v] and curr_dist + weight < distance[v]:
                distance[v] = curr_dist + weight
                parent[v] = u
                heapq.heappush(min_heap, (distance[v], v))

    # Reconstruct path
    path = []
    if distance[destination] == INF:
        return None, INF, visited_order  # No path found

    curr = destination
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path, distance[destination], visited_order


# ─────────────────────────────────────────────────────────
#  BFS  (Unweighted Shortest Path — fewest stops)
# ─────────────────────────────────────────────────────────
def bfs(graph, source, destination):
    """
    Finds shortest path in terms of number of hops (edges).
    Useful when all paths are considered equal (no weights).
    
    Returns:
        path     : list of node IDs from source to destination
        hops     : number of edges in the path
        visited_order : order in which nodes were explored
    """
    visited = set()
    parent = {}
    queue = deque([source])
    visited.add(source)
    parent[source] = -1
    visited_order = []

    while queue:
        u = queue.popleft()
        visited_order.append(u)

        if u == destination:
            break

        for v, _ in graph.get_neighbors(u):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    if destination not in parent:
        return None, -1, visited_order  # No path found

    # Reconstruct path
    path = []
    curr = destination
    while curr != -1:
        path.append(curr)
        curr = parent.get(curr, -1)
    path.reverse()

    return path, len(path) - 1, visited_order


# ─────────────────────────────────────────────────────────
#  A* ALGORITHM  (Heuristic-based shortest path)
# ─────────────────────────────────────────────────────────
def astar(graph, source, destination, heuristic=None):
    """
    A* search — combines Dijkstra with a heuristic for faster search.
    If no heuristic is provided, behaves like Dijkstra.
    
    The heuristic function: h(node) -> estimated distance to destination
    In a campus with no coordinate data, we use h=0 (same as Dijkstra).
    When you add GPS coordinates in higher semesters, plug in Euclidean distance.
    
    Returns:
        path : list of node IDs from source to destination
        cost : total path cost
        visited_order : exploration order
    """
    if heuristic is None:
        heuristic = lambda node: 0  # Default: no heuristic (acts like Dijkstra)

    INF = float('inf')
    num_nodes = max(graph.get_all_nodes()) + 1

    g_score = [INF] * num_nodes   # actual cost from source
    f_score = [INF] * num_nodes   # g + h
    g_score[source] = 0
    f_score[source] = heuristic(source)
    parent = [-1] * num_nodes
    closed = set()
    visited_order = []

    open_heap = [(f_score[source], source)]

    while open_heap:
        _, u = heapq.heappop(open_heap)

        if u in closed:
            continue
        closed.add(u)
        visited_order.append(u)

        if u == destination:
            break

        for v, weight in graph.get_neighbors(u):
            if v in closed:
                continue
            tentative_g = g_score[u] + weight
            if tentative_g < g_score[v]:
                g_score[v] = tentative_g
                f_score[v] = tentative_g + heuristic(v)
                parent[v] = u
                heapq.heappush(open_heap, (f_score[v], v))

    if g_score[destination] == INF:
        return None, INF, visited_order

    path = []
    curr = destination
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path, g_score[destination], visited_order