import math

def generate_execution_observation_table(sizes):
  result = [
    "Algorithm Execution Observation Table",
    "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
  ]
  
  def fibonacci_calls(n):
    if n <= 1:
      return 1
    return 1 + fibonacci_calls(n-1) + fibonacci_calls(n-2)

  for n in sizes:
    rec_factorial = n+1
    iter_factorial = n
    rec_fibonacci = fibonacci_calls(n)
    iter_fibonacci = n
    linear_search = n

    binary_search = math.floor(math.log2(n))+1 if n > 0 else 0

    bubble_sort = (n*(n-1))//2
    insertion_sort = (n*(n-1))//2

    row_values = [
      n,
      rec_factorial,
      iter_factorial,
      rec_fibonacci,
      iter_fibonacci,
      linear_search,
      binary_search,
      bubble_sort,
      insertion_sort
    ]
    result.append(" ".join(map(str,row_values)))

  return result