# Lab Question 1.1: Recursive vs Iterative Analysis

def analyze_recursive_iterative(n):
    # 1. Recursive factorial
    def factorial_recursive(x):
        if x <= 1:
            return 1
        return x * factorial_recursive(x - 1)

    rec_fact_val = factorial_recursive(n)
    rec_fact_count = n + 1

    # 2. Iterative factorial
    def factorial_iterative(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    iter_fact_val = factorial_iterative(n)
    iter_fact_count = n

    # 3. Recursive fibonacci
    rec_fib_count = 0

    def fibonacci_recursive(x):
        nonlocal rec_fib_count
        rec_fib_count += 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)

    rec_fib_val = fibonacci_recursive(n)

    # 4. Iterative fibonacci
    def fibonacci_iterative(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, x + 1):
            a, b = b, a + b
        return b

    iter_fib_val = fibonacci_iterative(n)
    iter_fib_count = n

    # Return output
    return [
        "Computation analysis report",
        f"Recursive factorial: {rec_fact_val}",
        f"Iterative factorial: {iter_fact_val}",
        f"Recursive fibonacci: {rec_fib_val}",
        f"Iterative fibonacci: {iter_fib_val}",
        "Operation count comparison",
        f"Recursive factorial: {rec_fact_count}",
        f"Iterative factorial: {iter_fact_count}",
        f"Recursive fibonacci: {rec_fib_count}",
        f"Iterative fibonacci: {iter_fib_count}",
    ]