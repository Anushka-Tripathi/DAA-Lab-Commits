# Problem 1.2: Compare Search Algorithms
def compare_search_algorithms(arr, target):
    # 1. Linear Search
    ls_index = -1
    ls_comp = 0
    for i in range(len(arr)):
        ls_comp += 1
        if arr[i] == target:
            ls_index = i
            break

    # 2. Binary Search (Finding First Occurrence)
    bs_index = -1
    bs_comp = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        bs_comp += 1
        if arr[mid] == target:
            bs_index = mid
            high = mid - 1  # Continue searching left for the first occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # 3. Determine the Better Algorithm
    if ls_comp < bs_comp:
        better = "Linear Search"
    elif bs_comp < ls_comp:
        better = "Binary Search"
    else:
        better = "Both Equal"

    # 4. Construct Output List of Strings
    result = [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {ls_index}",
        f"Comparisons: {ls_comp}",
        "Binary Search",
        f"Index: {bs_index}",
        f"Comparisons: {bs_comp}",
        f"Better Algorithm: {better}"
    ]

    return result

# Problem 1.3: Compare Sorting Algorithms
def compare_bubble_insertion(random_data, sorted_data, reverse_data):
    def bubble_sort(arr):
        data = list(arr)
        n = len(data)
        comparisons = 0
        swaps = 0

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swaps += 1
                    swapped = True
            # Optimized Bubble Sort: early stop if no elements were swapped
            if not swapped:
                break

        return data, comparisons, swaps

    def insertion_sort(arr):
        data = list(arr)
        n = len(data)
        comparisons = 0
        shifts = 0

        for i in range(1, n):
            key = data[i]
            j = i - 1

            while j >= 0:
                comparisons += 1
                if data[j] > key:
                    data[j + 1] = data[j]
                    shifts += 1
                    j -= 1
                else:
                    break
            data[j + 1] = key

        return data, comparisons, shifts

    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data),
    ]

    report = ["Sorting Performance Report"]

    for name, dataset in datasets:
        b_sorted, b_comp, b_swap = bubble_sort(dataset)
        i_sorted, i_comp, i_shift = insertion_sort(dataset)

        # Determine better algorithm based on fewer comparisons
        if b_comp < i_comp:
            better = "Bubble Sort"
        elif i_comp < b_comp:
            better = "Insertion Sort"
        else:
            better = "Both Equal"

        b_sorted_str = " ".join(map(str, b_sorted))
        i_sorted_str = " ".join(map(str, i_sorted))

        report.extend(
            [
                name,
                "Bubble Sort",
                f"Sorted: {b_sorted_str}",
                f"Comparisons: {b_comp}",
                f"Swaps: {b_swap}",
                "Insertion Sort",
                f"Sorted: {i_sorted_str}",
                f"Comparisons: {i_comp}",
                f"Shifts: {i_shift}",
                f"Better Algorithm: {better}",
            ]
        )

    return report