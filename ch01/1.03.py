def minmax(data):
    max = min = data[0]
    for d in data:
        if d > max:
            max = d
        else:
            min = d
    return min, max
input = input('Enter a list of numbers: ')
numbers = list(map(float, input.split()))
print('The smallest number is {value[0]: g}, the biggest number is {value[1]: g}.'.format(value = minmax(numbers)))
