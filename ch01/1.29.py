def perm(arr):
    #输入'c','a','t'
    #取出'c',返回['a','t'],['t','a']
    #得到['c','a','t'],['c','t','a']放入result
    #下一个循环,取出'a',返回['c','t'],['t','c']
    #得到['a','c','t'],['a','t','c']放入result
    result = []
    if len(arr) == 1:
        return [arr] #当arr只有一个字母的时候，返回一个数组
    else:
        for i in range(len(arr)):
            rest = arr[ :i] + arr[i+1: ] #取出第i个字母后得到剩下的数组
            list = perm(rest)
            for item in list:
                result.append(arr[i: i+1] + item)
        return result

input = input('Enter characters: ')
characters = input.split()
for item in perm(characters):
    s = ''.join(item)
    print(s + '\n')
