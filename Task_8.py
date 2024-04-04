# Create a loop that generates Fibonacci numbers up to a specified limit.
# my_range = [1, *range(1,15)]

a, b = 0, 1
series_length = 10
print(*range(series_length))


print(a, b, end=' ')
for i in range(series_length):
    c = a + b
    print(c, end=' ')
    a = b
    b = c