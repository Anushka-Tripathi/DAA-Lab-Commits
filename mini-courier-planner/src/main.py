import json
import os
import sys
from pathlib import Path

# Ensure src directory is in path regardless of working directory
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from benchmark import run_benchmarks
from graph_routing import nearest_neighbor_tsp
from knapsack_dp import solve_knapsack_dp
from models import DeliveryGraph, Parcel
from sorting import merge_sort_parcels


def load_dataset(filepath: Path) -> tuple[int, int, DeliveryGraph, list[Parcel]]:
    raw = json.loads(filepath.read_text(encoding="utf-8"))
    graph = DeliveryGraph()

    for node_id_str, name in raw["nodes"].items():
        graph.add_node(int(node_id_str), name)

    for u, v, dist in raw["edges"]:
        graph.add_edge(int(u), int(v), float(dist), bidirectional=True)

    parcels = [Parcel(**item) for item in raw["parcels"]]
    return int(raw["depot"]), int(raw["vehicle_capacity"]), graph, parcels


def main() -> None:
    os.chdir(PROJECT_ROOT)
    dataset_path = PROJECT_ROOT / "data" / "sample_dataset.json"
    depot, capacity, graph, parcels = load_dataset(dataset_path)

    print("=== PHASE 1 & 2: PARCEL PRIORITIZATION (MERGE SORT) ===")
    sorted_parcels = merge_sort_parcels(parcels)
    for p in sorted_parcels:
        print(
            f"  {p.parcel_id} | Tier: {p.priority_tier} | Deadline: {p.deadline_hours}h | "
            f"Weight: {p.weight}kg | Value: {p.value} | Dest: {graph.node_names[p.destination_id]}"
        )

    print(f"\n=== PHASE 2: OPTIMAL BOX FILLING (0/1 KNAPSACK, CAPACITY = {capacity}kg) ===")
    packing = solve_knapsack_dp(sorted_parcels, capacity)
    selected: list[Parcel] = packing["selected_parcels"]
    for p in selected:
        print(f"  [Selected] {p.parcel_id} -> {graph.node_names[p.destination_id]} ({p.weight}kg, val={p.value})")
    print(
        f"  Total Weight: {packing['total_weight']}/{capacity}kg | "
        f"Total Value: {packing['total_value']}"
    )

    print("\n=== PHASE 3: DIJKSTRA + NEAREST-NEIGHBOR TSP ROUTE ===")
    target_stops = [p.destination_id for p in selected]
    route_info = nearest_neighbor_tsp(graph, depot=depot, stop_nodes=target_stops)

    print("  Shortest Distances from Depot:")
    for node_id, dist in sorted(route_info["depot_distances"].items()):
        print(f"    Depot -> {graph.node_names[node_id]}: {dist} km")

    stop_names = [f"{nid} ({graph.node_names[nid]})" for nid in route_info["stop_sequence"]]
    print(f"  Ordered Delivery Stops: {' -> '.join(stop_names)}")
    print(f"  Full Road Path Nodes:   {route_info['expanded_route']}")
    print(f"  Total Tour Distance:    {route_info['total_distance']} km")

    # Run Phase 4 scaling benchmarks
    run_benchmarks()


if __name__ == "__main__":
    main()
