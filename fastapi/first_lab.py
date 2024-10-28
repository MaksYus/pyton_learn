import math
import cmath

def first(st:bool)->str:
    """
    Преобразует значение логической переменной в строку.

    >>> first(True)
    'True'
    >>> first(False)
    'False'
    """
    return str(st)

def second(string:str) -> str:
    """
    Принимает на вход строку и формирует из неё новую переписывая старую в обратном порядке
    >>> second('Hello World!')
    '!dlroW olleH'
    >>> second('Test2')
    '2tseT'
    """
    return string[::-1]

def third(array:list) -> float:
    """
    возвращает сумму всех положительных элементов массива
    >>> third([2,-1,9])
    11
    >>> third([1,-1,-1,-2])
    1
    """
    sum = 0
    for item in array:
        if (item > 0): sum += item 
    return sum

def forth(count:int) -> str:
    """
    возвращает строку, в формате ёлочки
    >>> forth(3)
    '  *\\n ***\\n*****\\n'
    >>> forth(2)
    ' *\\n***\\n'
    """
    if count < 0: count = 0
    string = ""
    for index in range(count):
        string+=(' '*(count-1-index) + '*'*(2*(index)+1))
        string+="\n"
    return string

def fifth(stri:str) -> int:
    """
    количество символов, которые встречаются в строке более одного раза
    >>> fifth("aabbccd")
    3
    >>> fifth("abcs")
    0
    """
    stri = stri.lower()
    dic = {}
    for l in stri:
        if(l in dic.keys()):
            dic[l]+=1
        else:
            dic[l] = 1
    count = 0
    for key in dic.keys():
        if(dic[key] >= 2):
            count +=1
    return count

def six(string:str) -> str:
    """
    Дана строка которая представлена в стиле camelCase.Напишите функцию которая преобразует данную строку в стиль kebab-case.
    >>> six("camelsHaveThreeHumps")
    'camels-have-three-humps'
    >>> six("ihi")
    'ihi'
    """
    index = 0
    for latter in string:
        if (latter.isupper()):
            newSubString = '-' + latter.lower()
            string = string.replace(latter,newSubString)
        index+=1
    return string

def seven(strin:int) -> str:
    """
    Дано целое число. Напишите функцию,которая преобразует число в другое по следующему принципу:
    >>> seven(1)
    '11'
    >>> seven(21)
    '1211'
    >>> seven(9000)
    '1930'
    """
    result = ''
    stri = str(strin)
    res_dic = {}
    for ch in stri:
        if ch in res_dic.keys():
            res_dic[ch] +=1
        else: res_dic[ch] = 1
    res_str = ""
    for key in res_dic.keys():
        res_str += str(res_dic[key]) + str(key)
    return res_str

def for_filter(x):
    return x % 2

def eight(array:list) -> list:
    """
    функция, которая сортирует все нечетные числа в массиве по возрастанию, при этом четные числа должны остаться на своих местах
    >>> eight([7,8,1])
    '[1, 8, 7]'
    >>> eight([2,4])
    '[2, 4]'
    """
    fil = filter(for_filter,array)
    fil = list(fil)
    fil.sort()
    index = 0
    index2 = 0
    for item in array:
        if item % 2 == 1: array[index2] = fil[index]; index+=1
        index2+=1
    return str(array)

def solve_ten(a:int,b:int,c:int,flag:bool) -> dict:
    """
    решает квадратные уравнения
    >>> solve_ten(-1,7,8,True)
    ((-1-0j), (8-0j))
    >>> solve_ten(-1,2,8,True)
    ((-2-0j), (4-0j))
    >>> solve_ten(2,0,2,True)
    (1j, -1j)
    """
    d = b*b - 4*a*c
    if not flag:
        try: d = math.sqrt(d)
        except: return None
    else: 
        d = cmath.sqrt(d)
    x1 = (0-b+d)/(2*a)
    x2 = (0-b-d)/(2*a)
    return {'x1 = ':x1,'x2 = ':x2}