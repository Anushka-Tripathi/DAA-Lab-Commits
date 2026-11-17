import heapq
from typing import Dict, List, Optional, Set, Tuple
from models import DeliveryGraph


def dijkstra(
    graph: DeliveryGraph, source: int
) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
    """
    Computes single-source shortest paths using a binary min-heap in O((V + E) log V).
    Returns distance map and predecessor map for path reconstruction.
    """
    distances: Dict[int, float] = {node: float("inf") for node in graph.nodes()}
    predecessors: Dict[int, Optional[int]] = {node: None for node in graph.nodes()}
    distances[source] = 0.0

    pq: List[Tuple[float, int]] = [(0.0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue

        for v, weight in graph.adj.get(u, []):
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                predecessors[v] = u
                heapq.heappush(pq, (new_dist, v))

    return distances, predecessors


def reconstruct_path(
    predecessors: Dict[int, Optional[int]], start: int, target: int
) -> List[int]:
    """Reconstructs the node-by-node path from start to target."""
    path: List[int] = []
    curr: Optional[int] = target
    while curr is not None:
        path.append(curr)
        if curr == start:
            break
        curr = predecessors[curr]
    path.reverse()
    return path if path and path[0] == start else []


def nearest_neighbor_tsp(
    graph: DeliveryGraph, depot: int, stop_nodes: List[int]
) -> Dict[str, object]:
    """
    Approximates an optimal delivery tour starting and ending at `depot`
    across all unique `stop_nodes` using shortest-path distances from Dijkstra.
    """
    unique_stops: Set[int] = set(stop_nodes) - {depot}
    relevant_nodes = [depot] + sorted(unique_stops)

    # Precompute Dijkstra shortest-path trees from all relevant stops
    dist_matrix: Dict[int, Dict[int, float]] = {}
    pred_matrix: Dict[int, Dict[int, Optional[int]]] = {}
    for node in relevant_nodes:
        d_map, p_map = dijkstra(graph, node)
        dist_matrix[node] = d_map
        pred_matrix[node] = p_map

    unvisited = set(unique_stops)
    current = depot
    stop_sequence: List[int] = [depot]
    expanded_route: List[int] = [depot]
    total_distance = 0.0

    while unvisited:
        next_stop = min(unvisited, key=lambda candidate: dist_matrix[current][candidate])
        leg_dist = dist_matrix[current][next_stop]
        if leg_dist == float("inf"):
            raise ValueError(f"Destination {next_stop} is unreachable from {current}.")

        leg_path = reconstruct_path(pred_matrix[current], current, next_stop)
        expanded_route.extend(leg_path[1:])
        total_distance += leg_dist

        stop_sequence.append(next_stop)
        unvisited.remove(next_stop)
        current = next_stop

    # Return to depot
    return_dist = dist_matrix[current][depot]
    if return_dist == float("inf"):
        raise ValueError(f"Depot {depot} is unreachable from {current}.")

    return_path = reconstruct_path(pred_matrix[current], current, depot)
    expanded_route.extend(return_path[1:])
    total_distance += return_dist
    stop_sequence.append(depot)

    return {
        "stop_sequence": stop_sequence,
        "expanded_route": expanded_route,
        "total_distance": round(total_distance, 2),
        "depot_distances": dist_matrix[depot],
    }
