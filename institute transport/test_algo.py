import sys
from campus_data import EDGES, get_all_locations
from graph import Graph
from algorithms import dijkstra, bfs

def test():
    g = Graph(directed=False)
    for u, v, w in EDGES:
        g.add_edge(u, v, w)

    path, cost, _ = dijkstra(g, 2, 26)
    print("Dijkstra Path:", path, "Cost:", cost)
    path_bfs, hops, _ = bfs(g, 2, 26)
    print("BFS Path:", path_bfs, "Hops:", hops)

if __name__ == "__main__":
    test()
