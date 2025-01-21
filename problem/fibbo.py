def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
    return fib_series

# Number of terms
n = int(input("Enter the number of terms: "))

# Generate Fibonacci series
fib_series = fibonacci(n)

# Print the Fibonacci series
print("Fibonacci Series:")
print(fib_series)
