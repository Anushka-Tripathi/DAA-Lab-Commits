def compare_bubble_insertion(random_data, sorted_data, reverse_data):
  def bubble_sort(arr):
    data = list(arr)
    n = len(data)
    comparisons = 0
    swaps = 0
    for i  in range(n):
      swapped = False
      for j in range(0, n-i-1):
        comparisons += 1
        if data[j] > data[j+1]:
          data[j], data[j+1] = data[j+1], data[j]
          swaps += 1
          swapped = True
      if not swapped:
        break
    return data, comparisons, swaps

  def insertion_sort(arr):
    data = list(arr)
    n = len(data)
    comparisons = 0
    shifts =  0
    for i in range(1,n):
      key = data[i]
      j = i-1
      while j >= 0:
        comparisons += 1
        if data[j] > key:
          data[j+1] = data[j]
          shifts += 1
          j -= 1
        else:
          break
      data[j+1] = key
    return data, comparisons, shifts

  result = ["Sorting Performance Report"]

  datasets = [
    ("Random Dataset", random_data),
    ("Sorted Dataset", sorted_data),
    ("Reverse Dataset", reverse_data)
  ]

  for item in datasets:
    label = item[0]
    data_arr = item[1]
    
    b_sorted, b_comp, b_swaps = bubble_sort(data_arr)
    i_sorted, i_comp, i_shifts = insertion_sort(data_arr)

    if b_comp < i_comp:
      better = "Bubble Sort"
    elif i_comp < b_comp:
      better = "Insertion Sort"
    else:
      better = "Both Equal"

    b_sorted_str = " ".join(map(str, b_sorted))
    i_sorted_str = " ".join(map(str, i_sorted))

    result.append(f"{label}")
    result.append(f"Bubble Sorted: {b_sorted_str}")
    result.append(f"Bubble Comparisons: {b_comp}")
    result.append(f"Bubble Swaps: {b_swaps}")
    result.append(f"Insertion Sorted: {i_sorted_str}")
    result.append(f"Insertion Comparisons: {i_comp}")
    result.append(f"Insertion Shifts: {i_shifts}")
    result.append(f"Better Algorithm: {better}")
    
  return result