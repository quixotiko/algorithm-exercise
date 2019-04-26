def are_they_distinct(data):
    numbers = set()
    for d in data:
        if d in numbers:
            return False
        else:
            numbers.add(d)
    return True

input = input('Enter a list of numbers: ')
print(are_they_distinct(input.split()))
