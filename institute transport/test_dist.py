import math
from campus_data import EDGES, GPS_COORDINATES

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000 # radius of earth in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def test():
    new_edges = []
    for u, v, w in EDGES:
        lat1, lon1 = GPS_COORDINATES[u]
        lat2, lon2 = GPS_COORDINATES[v]
        real_dist = round(haversine(lat1, lon1, lat2, lon2))
        new_edges.append((u, v, real_dist))
    
    # Check paths with new edges
    from collections import defaultdict
    import heapq
    
    graph = defaultdict(list)
    for u, v, w in new_edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    def dijkstra(src, dst):
        dist = {i: float('inf') for i in range(36)}
        dist[src] = 0
        parent = {i: -1 for i in range(36)}
        pq = [(0, src)]
        visited = set()
        while pq:
            d, u = heapq.heappop(pq)
            if u in visited: continue
            visited.add(u)
            if u == dst: break
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
        path = []
        curr = dst
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        return path, dist[dst]

    path, cost = dijkstra(2, 26)
    print("New Dijkstra Path:", path, "Cost:", cost)
    
    # Also print original cost of this new path
    orig_graph = defaultdict(list)
    for u, v, w in EDGES:
        orig_graph[u].append((v, w))
        orig_graph[v].append((u, w))
        
    print("Old Dijkstra Cost for old path [2, 3, 4, 6, 1, 31, 29, 25, 33, 26]:", sum(orig_graph[path[i]][0][1] for i in range(len(path)-1) if orig_graph[path[i]][0][0] == path[i+1] or True)) # rough
    print("New edges:")
    for e in new_edges:
        print(f"  {list(e)},")

if __name__ == "__main__":
    test()
