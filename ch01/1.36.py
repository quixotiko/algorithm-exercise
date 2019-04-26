def count(data):
    words = {}
    for d in data:
        if d not in words:
            words[d] = 1
        else:
            words[d] +=1
    return words

ws = input('Enter words: ')
data = ws.split()
words = count(data)
for k in words:
    print(k + ': appears ' + str(words[k]) + ' times')
