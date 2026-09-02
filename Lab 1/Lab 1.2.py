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