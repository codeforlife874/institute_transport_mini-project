# ui.py
# Command-line interface for the Institute Transport Route Optimizer

from campus_data import get_all_locations

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════╗
║    🏫 INSTITUTE TRANSPORT ROUTE OPTIMIZER                ║
║    Dayananda Sagar College of Engineering                ║
║    DSA Mini Project — 4th Semester                       ║
╚══════════════════════════════════════════════════════════╝
    """)

def show_locations():
    locations = get_all_locations()
    print("\n📌 Campus Locations:")
    print("-" * 40)
    for node_id, name in sorted(locations.items()):
        print(f"   [{node_id:2d}]  {name}")
    print("-" * 40)

def get_user_input():
    """Prompt the user to select source and destination."""
    show_locations()
    locations = get_all_locations()
    valid_ids = list(locations.keys())

    while True:
        try:
            src = int(input("\n➡️  Enter Source Location ID      : "))
            dst = int(input("➡️  Enter Destination Location ID : "))
            if src not in valid_ids:
                print(f"❌ Invalid source. Choose from {valid_ids}")
                continue
            if dst not in valid_ids:
                print(f"❌ Invalid destination. Choose from {valid_ids}")
                continue
            if src == dst:
                print("⚠️  Source and destination are the same. Try again.")
                continue
            return src, dst
        except ValueError:
            print("❌ Please enter a valid number.")

def choose_algorithm():
    """Let user pick which algorithm to use."""
    print("\n🧠 Choose Algorithm:")
    print("   [1] Dijkstra's Algorithm  (shortest distance, weighted)")
    print("   [2] BFS                   (fewest stops, unweighted)")
    print("   [3] A* Algorithm          (heuristic-based, fast)")
    print("   [4] Compare All Three")

    while True:
        choice = input("\n➡️  Enter choice [1-4]: ").strip()
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        print("❌ Invalid choice. Enter 1, 2, 3, or 4.")

def ask_visualize():
    """Ask if user wants a graph visualization."""
    ans = input("\n🖼️  Show visual graph? (y/n): ").strip().lower()
    return ans == 'y'

def ask_again():
    """Ask if user wants to find another route."""
    ans = input("\n🔄  Find another route? (y/n): ").strip().lower()
    return ans == 'y'