# Mini-Courier Planner (`ETCCDA302` Capstone Project)

**Course:** Design & Analysis of Algorithms (`ETCCDA302`)  
**Institution:** K.R. Mangalam University, Gurugram, Haryana  
**Programme:** B.Tech CSE (AI & ML)  
**Faculty:** Dr. Shweta Agarwal  

---

## Overview
Mini-Courier Planner is a Python prototype that simulates an intelligent courier dispatch engine. Given a set of customer parcels, vehicle weight capacity, and a road network graph, the system:
1. **Prioritizes** parcels by urgency tier and delivery deadline using **Merge Sort**.
2. **Optimizes** cargo loading for a single dispatch trip using **0/1 Knapsack Dynamic Programming**.
3. **Computes** shortest inter-stop road distances using **Dijkstra’s Algorithm**.
4. **Constructs** an ordered delivery tour starting and ending at the depot using a **Nearest-Neighbor TSP Approximation**.
5. **Benchmarks** runtime scaling across increasing workload sizes and generates a performance comparison chart.

---

## Project Structure
```text
mini-courier-planner/
├── data/
│   └── sample_dataset.json     # Sample road network & parcel workload
├── outputs/
│   └── runtime_chart.png       # Generated Phase 4 runtime scaling plot
├── src/
│   ├── __init__.py
│   ├── models.py               # Parcel dataclass & DeliveryGraph adjacency list
│   ├── sorting.py              # Stable O(n log n) Merge Sort implementation
│   ├── knapsack_dp.py          # O(n * W) 0/1 Knapsack DP + backtracking
│   ├── graph_routing.py        # Dijkstra's shortest paths & Nearest-Neighbor TSP
│   ├── benchmark.py            # Multi-scale performance testing & matplotlib export
│   └── main.py                 # End-to-end execution entry point
└── README.md
```

---

## Setup & Execution Steps
1. **Prerequisites:** Python 3.10+ (`matplotlib` optional for chart export).
   ```bash
   pip install matplotlib
   ```
2. **Run the Complete Pipeline & Benchmarks:**
   ```bash
   python src/main.py
   ```
3. **Outputs Produced:**
   - Sorted parcel manifest (Phase 2)
   - Optimal selected parcels, utilized weight, and total value (Phase 2)
   - Shortest distances from the depot, stop sequence, and full node-by-node road route (Phase 3)
   - Multi-size runtime table in console and `outputs/runtime_chart.png` (Phase 4)
