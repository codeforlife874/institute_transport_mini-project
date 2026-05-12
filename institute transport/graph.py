# graph.py
# Graph data structure using adjacency list representation

from campus_data import LOCATIONS, EDGES

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = {}   # { node: [(neighbor, weight), ...] }
        self.node_names = {}       # { node_id: name }

        # Initialize all nodes
        for node_id, name in LOCATIONS.items():
            self.add_node(node_id, name)

        # Add all edges from campus data
        for u, v, w in EDGES:
            self.add_edge(u, v, w)

    def add_node(self, node_id, name=""):
        if node_id not in self.adjacency_list:
            self.adjacency_list[node_id] = []
        self.node_names[node_id] = name

    def add_edge(self, u, v, weight=1):
        self.adjacency_list[u].append((v, weight))
        if not self.directed:
            self.adjacency_list[v].append((u, weight))

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def get_all_nodes(self):
        return list(self.adjacency_list.keys())

    def get_name(self, node_id):
        return self.node_names.get(node_id, str(node_id))

    def node_count(self):
        return len(self.adjacency_list)

    def edge_count(self):
        total = sum(len(neighbors) for neighbors in self.adjacency_list.values())
        return total if self.directed else total // 2

    def display(self):
        print("\n📍 Campus Graph (Adjacency List):")
        print("=" * 50)
        for node in sorted(self.adjacency_list.keys()):
            name = self.get_name(node)
            neighbors = self.get_neighbors(node)
            neighbor_str = ", ".join(
                f"{self.get_name(n)}({w}m)" for n, w in neighbors
            )
            print(f"  [{node}] {name:20s} → {neighbor_str}")
        print(f"\n  Total Nodes: {self.node_count()}")
        print(f"  Total Edges: {self.edge_count()}")