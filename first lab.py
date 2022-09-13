def first(st):
    return 'True' if st else 'False'

def second(string):
    return "".join(reversed(string))

def third(array):
    sum = 0
    for item in array:
        if (item > 0): sum += item 
    return sum

def forth(count):
    for index in range(count):
        print(' '*(count-1-index) + '*'*(2*(index)+1))

def fifth(stri):
    stri = stri.lower()
    dic = {}
    for l in stri:
        if(l in dic.keys()):
            dic[l]+=1
        else:
            dic[l] = 1
    keyMax = stri[0]
    for key in dic:
        if(dic[key] > dic[keyMax]):
            keyMax = key
    return dic[keyMax]

def six(string):
    index = 0
    for latter in string:
        if (latter.isupper()):
            newSubString = '-' + latter.lower()
            string = string.replace(latter,newSubString)
        index+=1
    return string

def seven(stri):
    result = ''
    lis = [(stri[0],1)]
    for index in range(1,len(stri)):
        if(stri[index] != stri[index-1]):
            lis.append((stri[index],1))
        else:
            lis[len(list)-1][1] += 1
    for item in lis:
        result = result + str(item[1])
        result = result + str(item[0])
    return result

def eight(array):
    #буду пузырьком
    

print('First')
print(first(False))
print(type(first(False)))
print('\nSecond')
print(second('Hello World!'))
print('\nThird')
print(third([2,-4,5,1,0,-10]))
print('\nForth')
forth(5)
print('\nFifth')
print(fifth('aabbccde'))
print('\nSix')
print(six('camelsHaveThreeHumps'))
print('\nSeven')
print(seven('123'))






