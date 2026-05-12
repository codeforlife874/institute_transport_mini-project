# main.py
# Entry point for Institute Transport Route Optimizer

from graph import Graph
from algorithms import dijkstra, bfs, astar
from visualizer import print_path_ascii, visualize_path
from ui import (
    print_banner, get_user_input,
    choose_algorithm, ask_visualize, ask_again
)

def run_algorithm(graph, src, dst, choice):
    results = []

    if choice == 1 or choice == 4:
        path, cost, _ = dijkstra(graph, src, dst)
        results.append(("Dijkstra's Algorithm", path, cost))

    if choice == 2 or choice == 4:
        path, hops, _ = bfs(graph, src, dst)
        # For BFS, cost is number of hops (not distance)
        results.append(("BFS (Fewest Stops)", path, hops))

    if choice == 3 or choice == 4:
        path, cost, _ = astar(graph, src, dst)
        results.append(("A* Algorithm", path, cost))

    return results

def main():
    print_banner()

    # Build the campus graph
    graph = Graph(directed=False)
    print(f"✅ Campus graph loaded: {graph.node_count()} locations, {graph.edge_count()} paths\n")

    while True:
        src, dst = get_user_input()
        choice = choose_algorithm()

        results = run_algorithm(graph, src, dst, choice)

        for algo_name, path, cost in results:
            unit = "meters" if "BFS" not in algo_name else "stops"
            print_path_ascii(graph, path, cost, algorithm=algo_name)

        # Visualization for the first result (or only result)
        if ask_visualize():
            first_path = results[0][1] if results else None
            first_algo = results[0][0] if results else "Route"
            visualize_path(graph, first_path, algorithm_name=first_algo)

        if not ask_again():
            print("\n👋 Thank you for using Institute Route Optimizer!")
            break

if __name__ == "__main__":
    main()