import os

def first(st:bool)->str:
    return str(st)

def second(string:str):
    return string[::-1]

def third(array):
    sum = 0
    for item in array:
        if (item > 0): sum += item 
    return sum

def forth(count):
    string = ""
    for index in range(count):
        string+=(' '*(count-1-index) + '*'*(2*(index)+1))
        string+="\n"
    return string

def fifth(stri):
    stri = stri.lower()
    dic = {}
    for l in stri:
        if(l in dic.keys()):
            dic[l]+=1
        else:
            dic[l] = 1
    count = 0
    for key in dic:
        if(dic[key] > 2):
            count +=1
    return count

def six(string):
    index = 0
    for latter in string:
        if (latter.isupper()):
            newSubString = '-' + latter.lower()
            string = string.replace(latter,newSubString)
        index+=1
    return string

def seven(strin):
    result = ''
    stri = str(strin)
    res_dic = {}
    for ch in stri:
        if ch in res_dic.keys():
            res_dic[ch] +=1
        else: res_dic[ch] = 1
    res_str = ""
    for key in res_dic.keys():
        res_str += str(key) + str(res_dic[key])
    return res_str

def for_filter(x):
    return x % 2

def eight(array):
    fil = filter(for_filter,array)
    fil = list(fil)
    fil.sort()
    index = 0
    index2 = 0
    for item in array:
        if item % 2 == 1: array[index2] = fil[index]; index+=1
        index2+=1
    return str(array)
    
def write_result(res, name:str):
    path = f"lab1\{name}.txt"
    print(path)
    try: os.remove(path)
    except: None
    file = open(path, "w")
    file.write(str(res[0]) + "\n")
    file.write(str(res[1]))
    file.close()


try:
    os.mkdir("lab1")
except: None
print('First')
print(first(False))
print(type(first(False)))
fir_1 = False
fir_2 = True
fir_res = []
fir_res.append(first(fir_1))
fir_res.append(first(fir_2))
write_result(fir_res,'1')
print('\nSecond')
print(second('Hello World!'))
sec_1 = 'Hello World!'
sec_2 = 'Bye World!'
sec_res = [second(sec_1),second(sec_2)]
write_result(sec_res,'2')
print('\nThird')
print(third([2,-4,5,1,0,-10]))
thi_1 = [2,-4,5,1,0,-10]
thi_2 = [1,2,3,-1,-2,-3,0]
th_res = [third(thi_1),third(thi_2)]
write_result(th_res,'3')
print('\nForth')
forth(5)
for_1 = 3
for_2 = 5
for_res = [forth(for_1),forth(for_2)]
write_result(for_res,'4')

print('\nFifth')

fiv_1 = 'aabbccde'
fiv_2 = 'indivisibilities'
print(fifth(fiv_2))
fiv_res = [str(fifth(fiv_1)),str(fifth(fiv_2))]
write_result(fiv_res,'5')

print('\nSix')
six_1 = 'camelsHaveThreeHumps'
six_2 = 'camelCase'
print(six('camelsHaveThreeHumps'))
six_res = [six(six_1),six(six_2)]
write_result(six_res,'6')
print('\nSeven')
print(seven('123'))
sev_1 = 123
sev_2 = 9000
res_sev_1 = seven(sev_1)
res_sev_2 = seven(sev_2)
sev_res = [res_sev_1,res_sev_2]
write_result(sev_res,'7')

print('\nEight')
eig_1 = [7, 8, 1]
eig_2 = [5, 8, 6, 3, 4]
eig_res = [eight(eig_1),eight(eig_2)]
write_result(eig_res,'8')
print(eight(eig_1))




