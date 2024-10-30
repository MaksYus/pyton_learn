class Calculator():
    def summation(self, num1: float, num2: float) -> float:
        return num1 + num2

    def subtraction(self, num1: float, num2: float) -> float:
        return num1 - num2

    def multiplication(self, num1: float, num2: float) -> float:
        return num1 * num2

    def division(self, num1: float, num2: float) -> float:
        return num1 / num2


def factorial(num: int) -> int:
    """
    Get factorial of number (num)
    if num is less then 0, it will return 0 
    """
    if (num == 0):
        return 1
    if (num < 0):
        return 0
    return num * factorial(num-1) if (num != 1) else 1

# ТЗ не четкое, задал вопрос HR, но ответа похоже не будет
# говорится, что "каждый следующий элемент должен быть равен предыдущему
# , но строго больше его" . Это два взаимоисключающих условия, как элемент должен быть синим, но строго красным


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[int(len(arr)/2)]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# бесконечный массив с конечным количеством элементов? это как?
# массивы в питоне и так бесконечные (почти, ограничено железом)
# окей, пускай будет просто массив с конечнм числом элементов как отдельный класс
# отдельно добавим приватное свойство max_len


class MyList(list):
    def __init__(self):
        self.__max_len: int = 0

    def max_len(self, *args) -> int:
        """
        Get max length of MyList. If args[0] is not None set max_length.
        """
        if ((len(args) == 1) and (type(args[0]) == int) and (args[0] > 0)):
            if (args[0] < len(self)):
                for _ in range(len(self)-args[0]):
                    super().pop()
            self.__max_len = args[0]
        return self.__max_len

    def append(self, object):
        """
        Add an item to the end of the list.   
        If length self equal max len, nothing will happen.
        """
        if len(self) == self.__max_len:
            return None
        return super().append(object)

    def extend(self, iterable):
        """
        Extend the list by appending all the items from the iterable.  
        If length iterable plus length self more then max len, nothing will happen
        """
        if (len(self) + len(iterable) > self.__max_len):
            return None
        return super().extend(iterable)

    def insert(self, index, object):
        """
        Insert an item at a given position.  
        If length iterable plus length self more then max len, nothing will happen
        """
        if len(self) == self.__max_len:
            return None
        return super().insert(index, object)


mlst = MyList()
print(mlst.max_len())
mlst.append(3)
print(mlst)
mlst.max_len(3)
mlst.append(1)
mlst.append(2)
mlst.append(3)
mlst.append(4)
print(mlst)
