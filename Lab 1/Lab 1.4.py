# Lab Question 1.5: Runtime Complexity Comparison

import math

def generate_runtime_complexity_table(n):
    linear_count = n
    binary_count = math.floor(math.log2(n)) + 1
    bubble_count = (n * (n - 1)) // 2
    insertion_count = (n * (n - 1)) // 2

    return [
        "Runtime Complexity Comparison",
        "Method ObservedCount ExpectedComplexity Observation",
        f"Linear Search {linear_count} O(n) Grows linearly",
        f"Binary Search {binary_count} O(log n) Grows logarithmically",
        f"Bubble Sort {bubble_count} O(n^2) Grows quadratically",
        f"Insertion Sort {insertion_count} O(n^2) Grows quadratically"
    ]

# Lab Question 1.6: Runtime Comparison Chart

def generate_runtime_chart_report(sizes):
    result = []

    result.append("Runtime Comparison Chart Data")
    result.append("InputSize LinearSearch BinarySearch BubbleSort InsertionSort")

    for n in sizes:
        linear_search = n

        binary_search = 1
        temp = n
        while temp > 1:
            temp //= 2
            binary_search += 1

        bubble_sort = n * (n - 1) // 2
        insertion_sort = n * (n - 1) // 2

        result.append(
            f"{n} {linear_search} {binary_search} "
            f"{bubble_sort} {insertion_sort}"
        )

    result.append("Scalability Summary")
    result.append("Algorithm Complexity Scalability")
    result.append("Linear Search O(n) Moderate")
    result.append("Binary Search O(log n) Excellent")
    result.append("Bubble Sort O(n^2) Poor")
    result.append("Insertion Sort O(n^2) Poor")

    result.append("Key Observations")
    result.append("Best Algorithm: Binary Search")
    result.append("Most Expensive Algorithm: Bubble Sort")
    result.append("Conclusion: Logarithmic algorithms scale better for large inputs")
    return result