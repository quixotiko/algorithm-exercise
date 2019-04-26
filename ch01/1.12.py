from random import randrange
def choice(data):
    index = randrange(0,len(data),1)
    return data[index]

input = input('Enter a list of numbers: ')
numbers = list(map(float, input.split()))
print('A random number is :', choice(numbers))
