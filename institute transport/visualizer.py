# visualizer.py
# Visualizes the campus graph and highlights the found path
# Uses matplotlib and networkx

def visualize_path(graph, path, algorithm_name="Dijkstra"):
    """
    Draws the full campus graph and highlights the shortest path.
    Requires: pip install matplotlib networkx
    """
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
    except ImportError:
        print("⚠️  Install libraries to visualize: pip install matplotlib networkx")
        return

    G = nx.Graph()

    # Add all nodes
    for node_id in graph.get_all_nodes():
        G.add_node(node_id, label=graph.get_name(node_id))

    # Add all edges
    added_edges = set()
    for node in graph.get_all_nodes():
        for neighbor, weight in graph.get_neighbors(node):
            edge = tuple(sorted((node, neighbor)))
            if edge not in added_edges:
                G.add_edge(node, neighbor, weight=weight)
                added_edges.add(edge)

    # Layout
    pos = nx.spring_layout(G, seed=42, k=2)

    plt.figure(figsize=(14, 9))
    plt.title(f"🏫 Institute Campus Route — {algorithm_name}", fontsize=14, fontweight='bold')

    # Draw all nodes and edges (background)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos,
                            labels={n: graph.get_name(n) for n in graph.get_all_nodes()},
                            font_size=7)
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=1.5, alpha=0.5)

    # Highlight shortest path
    if path and len(path) > 1:
        path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_nodes(G, pos, nodelist=path,
                               node_color='orange', node_size=1000)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                               edge_color='red', width=3)

        # Highlight source and destination
        nx.draw_networkx_nodes(G, pos, nodelist=[path[0]],
                               node_color='green', node_size=1200)
        nx.draw_networkx_nodes(G, pos, nodelist=[path[-1]],
                               node_color='crimson', node_size=1200)

    # Edge weight labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)

    # Legend
    from matplotlib.patches import Patch
    legend = [
        Patch(color='green',   label='Source'),
        Patch(color='crimson', label='Destination'),
        Patch(color='orange',  label='Path Node'),
        Patch(color='red',     label='Shortest Path'),
        Patch(color='gray',    label='Other Routes'),
    ]
    plt.legend(handles=legend, loc='upper left')

    plt.axis('off')
    plt.tight_layout()
    plt.savefig("campus_route.png", dpi=150)
    plt.show()
    print("📸 Graph saved as campus_route.png")


def print_path_ascii(graph, path, total_cost, algorithm="Dijkstra"):
    """Prints a simple ASCII representation of the path."""
    if not path:
        print("❌ No path found.")
        return

    print(f"\n{'='*55}")
    print(f"  🔍 Algorithm : {algorithm}")
    print(f"{'='*55}")
    print("  📍 Route:")
    for i, node in enumerate(path):
        name = graph.get_name(node)
        if i == 0:
            print(f"     🟢 START → {name}")
        elif i == len(path) - 1:
            print(f"     🔴 END   → {name}")
        else:
            print(f"     ➡️        → {name}")
    print(f"\n  📏 Total Distance : {total_cost} meters")
    print(f"  🚶 Number of Stops : {len(path) - 1}")
    print(f"{'='*55}")