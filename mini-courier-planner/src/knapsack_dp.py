from typing import Dict, List
from models import Parcel


def solve_knapsack_dp(parcels: List[Parcel], capacity: int) -> Dict[str, object]:
    """
    Solves the 0/1 Knapsack problem in O(n * W) time and O(n * W) space
    to select the maximum-value subset of parcels within vehicle capacity.
    """
    n = len(parcels)
    dp: List[List[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        p = parcels[i - 1]
        for w in range(capacity + 1):
            if p.weight <= w:
                include_val = p.value + dp[i - 1][w - p.weight]
                exclude_val = dp[i - 1][w]
                dp[i][w] = max(include_val, exclude_val)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected parcels
    selected: List[Parcel] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen = parcels[i - 1]
            selected.append(chosen)
            w -= chosen.weight

    selected.reverse()
    total_weight = sum(p.weight for p in selected)
    total_value = dp[n][capacity]

    return {
        "selected_parcels": selected,
        "total_weight": total_weight,
        "remaining_capacity": capacity - total_weight,
        "total_value": total_value,
        "dp_table": dp,
    }
