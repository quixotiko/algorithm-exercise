def sum_of_squares(n):
    return sum([n*n for n in range(0, n) if n%2 != 0])
input = input('Enter a positive integer: ')
n = int(input)
print('The sum is:',sum_of_squares(n))
