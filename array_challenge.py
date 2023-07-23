def array_challenge(arr):
    sum_val = sum(arr)

    fibonacci1, fibonacci2 = 0, 1
    fibonacci_sum = 0

    while fibonacci_sum < sum_val:
        fibonacci_sum = fibonacci1 + fibonacci2
        fibonacci1, fibonacci2 = fibonacci2, fibonacci_sum

    arr[0] = fibonacci_sum - sum_val
    return arr[0]

# Test the function with the example input
arr = [15, 1, 3]
output = array_challenge(arr)
print(output)  # Output: 2
