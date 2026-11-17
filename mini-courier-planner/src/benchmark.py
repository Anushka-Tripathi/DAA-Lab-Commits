import os
import random
import time
from typing import Dict, List

from graph_routing import nearest_neighbor_tsp
from knapsack_dp import solve_knapsack_dp
from models import DeliveryGraph, Parcel
from sorting import merge_sort_parcels


def generate_synthetic_case(
    num_parcels: int, num_nodes: int, seed: int = 42
) -> tuple[List[Parcel], DeliveryGraph, int]:
    """Generates random connected graphs and parcel workloads for scaling tests."""
    rng = random.Random(seed)
    graph = DeliveryGraph()

    # Build a spanning chain first so the graph is guaranteed connected
    for i in range(num_nodes):
        graph.add_node(i, f"Loc_{i}")
        if i > 0:
            graph.add_edge(i - 1, i, round(rng.uniform(2.0, 15.0), 1))

    # Add extra random cross-edges
    extra_edges = num_nodes * 2
    for _ in range(extra_edges):
        u = rng.randint(0, num_nodes - 1)
        v = rng.randint(0, num_nodes - 1)
        if u != v:
            graph.add_edge(u, v, round(rng.uniform(1.5, 20.0), 1))

    parcels: List[Parcel] = []
    for idx in range(1, num_parcels + 1):
        parcels.append(
            Parcel(
                parcel_id=f"PKG-{idx:04d}",
                deadline_hours=rng.randint(1, 48),
                priority_tier=rng.randint(1, 3),
                weight=rng.randint(1, 15),
                value=rng.randint(10, 100),
                destination_id=rng.randint(1, num_nodes - 1),
            )
        )

    capacity = max(25, num_parcels * 3)
    return parcels, graph, capacity


def run_benchmarks() -> List[Dict[str, float]]:
    """Measures runtime across escalating dataset sizes and exports a runtime chart."""
    configs = [
        (10, 8),
        (50, 20),
        (150, 40),
        (300, 60),
        (600, 80),
    ]
    results: List[Dict[str, float]] = []

    print("\n=== PHASE 4: PERFORMANCE BENCHMARKING ===")
    print(f"{'Parcels':>8} | {'Nodes':>6} | {'Sort (ms)':>10} | {'DP (ms)':>10} | {'Route (ms)':>11} | {'Total (ms)':>11}")
    print("-" * 70)

    for n_parcels, n_nodes in configs:
        parcels, graph, capacity = generate_synthetic_case(n_parcels, n_nodes)

        t0 = time.perf_counter()
        sorted_p = merge_sort_parcels(parcels)
        t1 = time.perf_counter()

        pack_res = solve_knapsack_dp(sorted_p, capacity)
        t2 = time.perf_counter()

        stops = [p.destination_id for p in pack_res["selected_parcels"]]
        _ = nearest_neighbor_tsp(graph, depot=0, stop_nodes=stops)
        t3 = time.perf_counter()

        sort_ms = (t1 - t0) * 1000
        dp_ms = (t2 - t1) * 1000
        route_ms = (t3 - t2) * 1000
        total_ms = (t3 - t0) * 1000

        results.append(
            {
                "parcels": n_parcels,
                "nodes": n_nodes,
                "sort_ms": sort_ms,
                "dp_ms": dp_ms,
                "route_ms": route_ms,
                "total_ms": total_ms,
            }
        )
        print(
            f"{n_parcels:8d} | {n_nodes:6d} | {sort_ms:10.3f} | {dp_ms:10.3f} | {route_ms:11.3f} | {total_ms:11.3f}"
        )

    _save_chart(results)
    return results


def _save_chart(results: List[Dict[str, float]]) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n[Info] matplotlib not installed; skipping PNG chart generation.")
        return

    os.makedirs("outputs", exist_ok=True)
    x = [r["parcels"] for r in results]
    plt.figure(figsize=(8, 5))
    plt.plot(x, [r["sort_ms"] for r in results], marker="o", label="Merge Sort O(n log n)")
    plt.plot(x, [r["dp_ms"] for r in results], marker="s", label="0/1 Knapsack DP O(nW)")
    plt.plot(x, [r["route_ms"] for r in results], marker="^", label="Dijkstra + NN-TSP")
    plt.title("Mini-Courier Planner Runtime Scaling")
    plt.xlabel("Number of Parcels")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("outputs/runtime_chart.png", dpi=150)
    print("\n[Saved] Runtime comparison chart -> outputs/runtime_chart.png")
