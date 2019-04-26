def is_multiple(n, m):
    return True if n % m == 0 else False

input = input('Enter two numbers: ')
numbers = input.split( )
n = float(numbers[0])
m = float(numbers[1])
print(is_multiple(n, m))
