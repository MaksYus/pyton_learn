import first_lab as fl

def test_one():
    assert fl.first(True) == "True"
    assert fl.first(False) == "False"
def test_two():
    assert fl.second('Hello, world!') == "!dlrow ,olleH"
    assert fl.second('Test2') == "2tseT"
def test_3():
    assert fl.third([2, -4, 5, 1, 0, -10]) == 8
    assert fl.third([2,-1,9]) == 11
def test_4():
    assert fl.forth(3) == '  *\n ***\n*****\n'
def test_5():
    assert fl.fifth('aabbccd') == 3
def test_6():
    assert fl.six('camelsHaveThreeHumps') == 'camels-have-three-humps'
def test_7():
    assert fl.seven(9000) == '1930'
    assert fl.seven(21) == '1211'
def test_8():
    assert fl.eight([7,8,1]) == '[1, 8, 7]'
    assert fl.eight([5, 8, 6, 3, 4]) == '[3, 8, 6, 5, 4]'
    assert fl.eight([2,4]) == '[2, 4]'
def test_10():
    assert fl.solve_ten(-1,7,8,True) == ((-1-0j), (8-0j))
    assert fl.solve_ten(-1,2,8,True) == ((-2-0j), (4-0j))
    assert fl.solve_ten(2,0,2,True) == ((0+1j), (0-1j))