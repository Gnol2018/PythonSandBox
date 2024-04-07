# Calculate fibonannci number in F(n) when n > 1
# Iterative approach
def fibonacci_iterative(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    fibonacci_0 = 0
    fibonacci_1 = 1
    # find the next number
    for i in range(2, n + 1):
       # This define the next number
       fibonacci_next = fibonacci_0 + fibonacci_1
       # now the first number will be one
       fibonacci_0 = fibonacci_1
       # 1 will be next
       fibonacci_1 = fibonacci_next
    return fibonacci_1

print(fibonacci_iterative(6))
