from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Parcel:
    """Represents a single delivery parcel with priority, capacity, and destination attributes."""
    parcel_id: str
    deadline_hours: int      # Lower value = more urgent deadline
    priority_tier: int       # 1 = High, 2 = Medium, 3 = Low
    weight: int              # Capacity consumed in integer units (e.g., kg)
    value: int               # Business/urgency value used in Knapsack optimization
    destination_id: int      # Target node ID in the customer delivery graph


class DeliveryGraph:
    """Weighted undirected/directed graph using an adjacency list representation."""

    def __init__(self) -> None:
        self.adj: Dict[int, List[Tuple[int, float]]] = {}
        self.node_names: Dict[int, str] = {}

    def add_node(self, node_id: int, name: str = "") -> None:
        if node_id not in self.adj:
            self.adj[node_id] = []
        self.node_names[node_id] = name or f"Node_{node_id}"

    def add_edge(self, u: int, v: int, distance: float, bidirectional: bool = True) -> None:
        if distance < 0:
            raise ValueError("Dijkstra's algorithm requires non-negative edge weights.")
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, distance))
        if bidirectional:
            self.adj[v].append((u, distance))

    def nodes(self) -> List[int]:
        return sorted(self.adj.keys())
